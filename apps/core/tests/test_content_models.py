from django.utils import translation

import pytest

from apps.core.models import Certification, Experience, Project, SkillCategory


@pytest.mark.django_db
class TestSeededContent:
    """A migration de carga deve popular o conteúdo do portfólio."""

    def test_seed_populates_all_models(self):
        assert SkillCategory.objects.count() == 7
        assert Project.objects.count() == 11
        assert Experience.objects.count() == 4
        assert Certification.objects.count() == 8

    def test_projects_are_ordered(self):
        titles = list(Project.objects.values_list("title", flat=True))
        assert titles[0] == "API Encurtador de Links"
        assert titles[-1] == "E-commerce Ibeize"


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

    def test_repo_name_extracted_from_url(self):
        project = Project.objects.get(title="Portfólio Pessoal")
        assert project.repo_name == "portfolio_davi_oliveira"


@pytest.mark.django_db
class TestExperienceHelpers:
    def test_details_list_splits_lines(self):
        experience = Experience.objects.get(company="iBeize")
        assert len(experience.details_list) == 4

    def test_details_translated(self):
        with translation.override("en"):
            experience = Experience.objects.get(company="iBeize")
            assert experience.details_list[0].startswith("Results analysis")
