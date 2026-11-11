from importlib import import_module
from types import SimpleNamespace

from django.apps import apps
from django.conf import settings
from django.db import connection
from django.utils import translation

import pytest

from apps.core.models import Certification, Experience, Project, SkillCategory


def _undo_hiper_split(editor):
    # Migrações anteriores à 0032 localizam a Hiper só pela empresa e esperam
    # uma única experiência; revertê-las exige desfazer a separação antes.
    import_module("apps.core.migrations.0032_split_hiper_experience").restore_content(
        apps, editor
    )


@pytest.mark.django_db
class TestSeededContent:
    """A migration de carga deve popular o conteúdo do portfólio."""

    def test_seed_populates_all_models(self):
        assert SkillCategory.objects.count() == 6
        assert Project.objects.count() == 6
        assert Experience.objects.count() == 6
        assert Certification.objects.count() == 9

    def test_projects_follow_resume_then_portfolio_then_collections(self):
        assert list(Project.objects.values_list("title", flat=True)) == [
            "Apex Acelera | Reports",
            "Atalho Prancheta",
            "E-commerce iBeize",
            "Portfólio Pessoal",
            "Projetos Python",
            "Projetos de Ciência de Dados",
        ]

    def test_projects_by_category(self):
        by_category = {}
        for title, category in Project.objects.values_list("title", "category"):
            by_category.setdefault(category, []).append(title)
        assert by_category == {
            "empresarial": ["Apex Acelera | Reports", "E-commerce iBeize"],
            "tecnico": [
                "Atalho Prancheta",
                "Projetos Python",
                "Projetos de Ciência de Dados",
            ],
            "sites": ["Portfólio Pessoal"],
        }

    def test_certifications_list_newest_first(self):
        ids = list(Certification.objects.values_list("id", flat=True))
        assert ids == sorted(ids, reverse=True)

    def test_order_field_pins_item_to_the_top(self):
        oldest = Project.objects.order_by("id").first()
        oldest.order = 99
        oldest.save(update_fields=["order"])
        assert Project.objects.first() == oldest


@pytest.mark.django_db
class TestTranslatableFields:
    def test_returns_portuguese_by_default(self):
        with translation.override("pt-br"):
            project = Project.objects.get(github_url__endswith="python-projects")
            assert project.title_i18n == "Projetos Python"

    def test_returns_english_when_active(self):
        with translation.override("en"):
            project = Project.objects.get(github_url__endswith="python-projects")
            assert project.title_i18n == "Python Projects"

    def test_falls_back_to_portuguese_without_translation(self):
        with translation.override("en"):
            project = Project.objects.get(
                github_url__endswith="portfolio_davi_oliveira"
            )
            # tags_en vazio → usa tags PT
            assert "Deploy VPS" in project.tag_list


@pytest.mark.django_db
class TestProjectHelpers:
    def test_tag_list_splits_and_strips(self):
        project = Project.objects.get(github_url__endswith="atalho-prancheta")
        assert project.tag_list == ["Django", "DRF", "PostgreSQL", "Redis"]

    def test_every_project_has_a_preview(self):
        assert not Project.objects.filter(image="").exists()

    def test_collections_use_generated_covers(self):
        covers = dict(
            Project.objects.filter(
                github_url__regex=r"(python-projects|data_science_projects)$"
            ).values_list("github_url", "image")
        )
        assert sorted(covers.values()) == [
            "images/projects/data-science-projects.webp",
            "images/projects/python-projects.webp",
        ]

    def test_preview_paths_point_to_static_files(self):
        for path in Project.objects.exclude(image="").values_list("image", flat=True):
            assert (settings.BASE_DIR / "static" / path).exists()

    def test_apex_uses_webp_preview_and_hides_private_repo(self):
        project = Project.objects.get(title="Apex Acelera | Reports")
        assert project.image == "images/projects/apex-reports.webp"
        # Repositório privado: sem URL, o card não mostra o botão "Código"
        assert project.github_url == ""

    def test_repo_name_extracted_from_url(self):
        project = Project.objects.get(title="Portfólio Pessoal")
        assert project.repo_name == "portfolio_davi_oliveira"

    def test_project_descriptions_are_short_complete_previews(self):
        for project in Project.objects.all():
            assert project.description.endswith("."), project.title
            assert project.description_en.endswith("."), project.title
            assert len(project.description) <= 180, project.title
            assert len(project.description_en) <= 180, project.title
            if project.image:
                assert len(project.description) <= 100, project.title
                assert len(project.description_en) <= 100, project.title


@pytest.mark.django_db
class TestExperienceHelpers:
    def test_details_list_splits_lines(self):
        experience = Experience.objects.get(company="iBeize")
        assert len(experience.details_list) == 4

    @pytest.mark.parametrize("language", ["pt-br", "en"])
    @pytest.mark.parametrize(
        "company,role,count",
        [
            ("Apex Acelera", "", 3),
            ("iBeize", "", 4),
            ("Hiper Morada Nova", "Assistente Administrativo", 2),
            ("Hiper Morada Nova", "Jovem Aprendiz", 1),
            ("Betânia Lácteos", "", 1),
            ("Prisma Informática", "", 1),
        ],
    )
    def test_experience_keeps_requested_details(self, company, role, count, language):
        with translation.override(language):
            # role vazio casa com qualquer cargo (empresas com uma só experiência)
            experience = Experience.objects.get(company=company, role__contains=role)
            assert len(experience.details_list) == count
            assert all(not detail.startswith("•") for detail in experience.details_list)

    def test_hiper_is_split_into_two_roles_like_the_resume(self):
        assistant, apprentice = Experience.objects.filter(company="Hiper Morada Nova")
        assert (assistant.role, assistant.period) == (
            "Assistente Administrativo",
            "Abr 2022 a Abr 2025 · Morada Nova, CE",
        )
        assert assistant.details_list == [
            "Gerenciei o ciclo de NF-e via SysPDV, com conferência tributária e "
            "conformidade fiscal diária",
            "Desenvolvi dashboards e relatórios automatizados em Excel, "
            "transformando dados brutos em insights de negócio",
        ]
        assert (apprentice.role, apprentice.period) == (
            "Jovem Aprendiz",
            "Abr 2021 a Abr 2022 · Morada Nova, CE",
        )
        assert apprentice.details_list == [
            "Organizei boletos e processos administrativos e ofereci suporte "
            "técnico básico",
        ]

    def test_experiences_follow_resume_order(self):
        assert list(Experience.objects.values_list("company", "role")) == [
            ("Apex Acelera", "Gestor de Dados e Tráfego Pago"),
            ("iBeize", "Analista de E-commerce"),
            ("Hiper Morada Nova", "Assistente Administrativo"),
            ("Hiper Morada Nova", "Jovem Aprendiz"),
            ("Betânia Lácteos", "Jovem Aprendiz"),
            ("Prisma Informática", "Estagiário de TI"),
        ]

    def test_hiper_split_is_reversible(self):
        migration = import_module("apps.core.migrations.0032_split_hiper_experience")
        editor = SimpleNamespace(connection=connection)

        migration.restore_content(apps, editor)
        experience = Experience.objects.get(company="Hiper Morada Nova")
        for field, value in migration.ASSISTANT[0].items():
            assert getattr(experience, field) == value, field
        assert Experience.objects.get(company="Prisma Informática").order == 4

        migration.apply_content(apps, editor)
        assert Experience.objects.filter(company="Hiper Morada Nova").count() == 2
        assert Experience.objects.get(company="Prisma Informática").order == 5

    def test_ibeize_and_prisma_include_requested_web_technologies(self):
        ibeize = Experience.objects.get(company="iBeize")
        prisma = Experience.objects.get(company="Prisma Informática")
        assert "CSS/HTML/JS/GoTemplate avançado" in ibeize.details_list[1]
        assert "integração com operação logística" in ibeize.details_list[3]
        assert prisma.role == "Estagiário de TI"
        assert "primeiro contato com desenvolvimento web" in prisma.details_list[0]

    def test_content_update_is_reversible(self):
        # Migrações posteriores (0027, 0029) reescrevem parte desses textos,
        # então o teste recria o estado que a 0025 deixou antes de revertê-la.
        migration = import_module(
            "apps.core.migrations.0025_refresh_experience_details_and_apex_image"
        )
        editor = SimpleNamespace(connection=connection)
        _undo_hiper_split(editor)
        migration.apply_content(apps, editor)
        migration.restore_content(apps, editor)
        for company, (details, details_en) in migration.OLD_DETAILS.items():
            experience = Experience.objects.get(company=company)
            assert (experience.details, experience.details_en) == (details, details_en)
        assert (
            Project.objects.get(title=migration.PROJECT_TITLE).image
            == migration.OLD_IMAGE
        )

        migration.apply_content(apps, editor)
        for company, (details, details_en) in migration.NEW_DETAILS.items():
            experience = Experience.objects.get(company=company)
            assert (experience.details, experience.details_en) == (details, details_en)
        assert (
            Project.objects.get(title=migration.PROJECT_TITLE).image
            == migration.NEW_IMAGE
        )

    def test_resume_update_is_reversible(self):
        migration = import_module("apps.core.migrations.0029_match_new_resume")
        editor = SimpleNamespace(connection=connection)
        _undo_hiper_split(editor)

        migration.restore_content(apps, editor)
        assert SkillCategory.objects.count() == len(migration.OLD_CATEGORIES)
        for company, (before, _after) in migration.EXPERIENCES.items():
            experience = Experience.objects.get(company=company)
            for field, value in before.items():
                assert getattr(experience, field) == value, (company, field)
        shortener = Project.objects.get(github_url__endswith="url_shortener_api")
        assert shortener.title == "API Encurtador de Links"
        assert shortener.order == 0

        migration.apply_content(apps, editor)
        assert SkillCategory.objects.count() == len(migration.NEW_CATEGORIES)
        for company, (_before, after) in migration.EXPERIENCES.items():
            experience = Experience.objects.get(company=company)
            for field, value in after.items():
                assert getattr(experience, field) == value, (company, field)
        shortener = Project.objects.get(github_url__endswith="atalho-prancheta")
        assert shortener.title == "Atalho Prancheta"
        assert shortener.order == 2

    def test_project_curation_is_reversible(self):
        migration = import_module("apps.core.migrations.0030_curate_projects")
        editor = SimpleNamespace(connection=connection)
        removed = [p["github_url"] for p in migration.REMOVED_PROJECTS]

        migration.restore_content(apps, editor)
        assert Project.objects.filter(github_url__in=removed).count() == 6
        restored = Project.objects.get(github_url__endswith="daily_diet_api")
        assert restored.tags_en == "Flask, SQLite, Pytest, 95% coverage"
        assert Project.objects.get(github_url__endswith="python-projects").image == ""
        apex = Project.objects.get(title="Apex Acelera | Reports")
        assert apex.github_url.endswith("/apex-reports")
        assert apex.image == "images/projects/apex-reports-overview.png"

        migration.apply_content(apps, editor)
        assert not Project.objects.filter(github_url__in=removed).exists()
        assert Project.objects.count() == 6
        apex.refresh_from_db()
        assert (apex.github_url, apex.image) == (
            "",
            "images/projects/apex-reports.webp",
        )

    def test_ecommerce_control_removal_is_reversible(self):
        migration = import_module("apps.core.migrations.0031_remove_ecommerce_control")
        editor = SimpleNamespace(connection=connection)

        migration.restore_content(apps, editor)
        project = Project.objects.get(title="Ecommerce Control")
        assert project.order == 5
        assert project.image == "images/projects/ecommerce-control.webp"
        assert Project.objects.count() == 7

        migration.apply_content(apps, editor)
        assert not Project.objects.filter(title="Ecommerce Control").exists()
        assert Project.objects.count() == 6

    def test_ibeize_period_is_closed(self):
        experience = Experience.objects.get(company="iBeize")
        assert experience.period.startswith("Fev 2026 a Jul 2026")
        assert experience.period_en.startswith("Feb 2026 to Jul 2026")

    def test_current_role_comes_first(self):
        assert Experience.objects.first().company == "Apex Acelera"

    def test_current_role_matches_resume(self):
        experience = Experience.objects.get(company="Apex Acelera")
        assert experience.role == "Gestor de Dados e Tráfego Pago"
        with translation.override("en"):
            assert experience.role_i18n == "Data and Paid Traffic Manager"

    def test_apex_role_update_is_reversible(self):
        migration = import_module("apps.core.migrations.0033_apex_role_matches_resume")
        editor = SimpleNamespace(connection=connection)

        migration.revert_role(apps, editor)
        experience = Experience.objects.get(company="Apex Acelera")
        assert (experience.role, experience.role_en) == (
            migration.OLD_ROLE,
            migration.OLD_ROLE_EN,
        )

        migration.apply_role(apps, editor)
        experience.refresh_from_db()
        assert (experience.role, experience.role_en) == (
            migration.NEW_ROLE,
            migration.NEW_ROLE_EN,
        )

    def test_current_role_period_is_open_and_remote(self):
        experience = Experience.objects.get(company="Apex Acelera")
        assert experience.period == "Ago 2026 até hoje · Remoto"
        assert experience.period_en == "Aug 2026 to present · Remote"

    def test_details_translated(self):
        with translation.override("en"):
            experience = Experience.objects.get(company="iBeize")
            assert experience.details_list[0].startswith("Results analysis")
