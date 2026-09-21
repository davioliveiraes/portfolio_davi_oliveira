from importlib import import_module
from types import SimpleNamespace

from django.apps import apps
from django.conf import settings
from django.db import connection
from django.utils import translation

import pytest

from apps.core.models import Certification, Experience, Project, SkillCategory


@pytest.mark.django_db
class TestSeededContent:
    """A migration de carga deve popular o conteúdo do portfólio."""

    def test_seed_populates_all_models(self):
        assert SkillCategory.objects.count() == 6
        assert Project.objects.count() == 13
        assert Experience.objects.count() == 5
        assert Certification.objects.count() == 9

    def test_projects_list_newest_first(self):
        ids = list(Project.objects.values_list("id", flat=True))
        assert ids == sorted(ids, reverse=True)

    def test_certifications_list_newest_first(self):
        ids = list(Certification.objects.values_list("id", flat=True))
        assert ids == sorted(ids, reverse=True)

    def test_order_field_pins_item_to_the_top(self):
        oldest = Project.objects.order_by("id").first()
        oldest.order = 1
        oldest.save(update_fields=["order"])
        assert Project.objects.first() == oldest


@pytest.mark.django_db
class TestTranslatableFields:
    def test_returns_portuguese_by_default(self):
        with translation.override("pt-br"):
            project = Project.objects.get(github_url__endswith="jwt_order_api")
            assert project.title_i18n == "API de Pedidos com JWT"

    def test_returns_english_when_active(self):
        with translation.override("en"):
            project = Project.objects.get(github_url__endswith="jwt_order_api")
            assert project.title_i18n == "JWT Order API"

    def test_falls_back_to_portuguese_without_translation(self):
        with translation.override("en"):
            project = Project.objects.get(github_url__endswith="pet_adoption_api")
            # tags_en vazio → usa tags PT
            assert "Clean Architecture" in project.tag_list


@pytest.mark.django_db
class TestProjectHelpers:
    def test_tag_list_splits_and_strips(self):
        project = Project.objects.get(github_url__endswith="url_shortener_api")
        assert project.tag_list == ["Django REST Framework", "PostgreSQL", "Docker"]

    def test_projects_with_interface_have_a_preview(self):
        with_preview = set(
            Project.objects.exclude(image="").values_list("title", flat=True)
        )
        assert with_preview == {
            "Apex Acelera | Reports",
            "Ecommerce Control",
            "E-commerce Ibeize",
            "Portfólio Pessoal",
        }

    def test_preview_paths_point_to_static_files(self):
        for path in Project.objects.exclude(image="").values_list("image", flat=True):
            assert (settings.BASE_DIR / "static" / path).exists()

    def test_apex_uses_updated_screenshot(self):
        project = Project.objects.get(title="Apex Acelera | Reports")
        assert project.image == "images/projects/apex-reports-overview.png"

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
        "company,count",
        [
            ("Apex Acelera", 3),
            ("iBeize", 4),
            ("Hiper Morada Nova", 4),
            ("Betânia Lácteos", 2),
            ("Prisma Informática", 2),
        ],
    )
    def test_experience_keeps_requested_details(self, company, count, language):
        with translation.override(language):
            experience = Experience.objects.get(company=company)
            assert len(experience.details_list) == count
            assert all(not detail.startswith("•") for detail in experience.details_list)

    def test_hiper_includes_fiscal_work_and_updated_reporting_description(self):
        experience = Experience.objects.get(company="Hiper Morada Nova")
        assert experience.details_list == [
            "Gerenciei o ciclo completo de entrada e saída de NF-e via SysPDV, "
            "garantindo correta emissão, conferência tributária e conformidade "
            "fiscal diária.",
            "Desenvolvi e implementei dashboards automatizados em Excel, "
            "transformando dados brutos em insights de negócio.",
            "Automatizei análises e relatórios administrativos, melhorando a "
            "precisão e eficiência operacional.",
            "Prestei suporte técnico a sistemas e equipamentos, garantindo a "
            "continuidade operacional do SysPDV.",
        ]
        assert "60%" not in experience.details_en

    def test_ibeize_and_prisma_include_requested_web_technologies(self):
        ibeize = Experience.objects.get(company="iBeize")
        prisma = Experience.objects.get(company="Prisma Informática")
        assert "CSS/HTML/JS/GoTemplate avançado" in ibeize.details_list[1]
        assert "integração com operação logística" in ibeize.details_list[3]
        assert "HTML5, CSS3 e JavaScript" in prisma.details_list[0]
        assert "integração front-end e back-end." in prisma.details_list[0]

    def test_content_update_is_reversible(self):
        migration = import_module(
            "apps.core.migrations.0025_refresh_experience_details_and_apex_image"
        )
        editor = SimpleNamespace(connection=connection)
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

    def test_ibeize_period_is_closed(self):
        experience = Experience.objects.get(company="iBeize")
        assert experience.period.startswith("Fev 2026 a Jul 2026")
        assert experience.period_en.startswith("Feb 2026 to Jul 2026")

    def test_current_role_comes_first(self):
        assert Experience.objects.first().company == "Apex Acelera"

    def test_current_role_period_is_open_and_remote(self):
        experience = Experience.objects.get(company="Apex Acelera")
        assert experience.period == "Ago 2026 até hoje · Remoto"
        assert experience.period_en == "Aug 2026 to today · Remote"

    def test_details_translated(self):
        with translation.override("en"):
            experience = Experience.objects.get(company="iBeize")
            assert experience.details_list[0].startswith("Results analysis")
