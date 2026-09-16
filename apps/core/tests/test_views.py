from unittest.mock import patch

from django.test import Client
from django.urls import reverse
from django.utils.translation import override

import pytest

from apps.core.models import Contact


@pytest.mark.django_db
class TestHomePage:
    """A one-page renderiza todas as seções em uma única resposta."""

    def test_home_returns_200(self, client: Client):
        response = client.get(reverse("core:home"))
        assert response.status_code == 200

    def test_home_uses_one_page_template(self, client: Client):
        response = client.get(reverse("core:home"))
        templates = [t.name for t in response.templates]
        assert "core/home.html" in templates
        assert "base.html" in templates

    def test_home_context_has_all_sections(self, client: Client):
        response = client.get(reverse("core:home"))
        for key in ("experiences", "categories", "projects", "certifications", "form"):
            assert key in response.context

    def test_home_contains_section_anchors(self, client: Client):
        html = client.get(reverse("core:home")).content.decode()
        for anchor in (
            'id="inicio"',
            'id="experiencia"',
            'id="habilidades"',
            'id="projetos"',
            'id="formacao"',
            'id="contatos"',
        ):
            assert anchor in html

    def test_home_renders_seeded_content(self, client: Client):
        html = client.get(reverse("core:home")).content.decode()
        assert "Ecommerce Control" in html
        assert "iBeize" in html

    @pytest.mark.parametrize("language", ["pt-br", "en"])
    def test_resume_download_uses_profile_filename(self, client, language):
        with override(language):
            html = client.get(reverse("core:home")).content.decode()
        assert (
            '<a href="/static/docs/curriculo.pdf" '
            'download="davi-oliveira-profile.pdf" id="cvButton"'
        ) in html

    def test_hero_preserves_identity_and_actions(self, client: Client):
        html = client.get(reverse("core:home")).content.decode()
        hero = html.split('<section id="inicio"', 1)[1].split("</section>", 1)[0]

        assert 'aria-labelledby="hero-title"' in hero
        assert 'id="hero-title"' in hero
        assert "images/profile-cutout.webp" in hero
        assert 'alt="Davi Oliveira"' in hero
        assert 'href="#projetos"' in hero
        assert 'href="#contatos"' in hero
        assert 'class="hero-tech"' in hero
        assert 'class="hero-circuit"' in hero
        assert 'aria-hidden="true" focusable="false"' in hero
        for layer in ("backend", "data", "ai"):
            assert f'class="hero-art-{layer}"' in hero

    @pytest.mark.parametrize(
        "language,title,accent",
        [
            ("pt-br", "Programação e Dados", "Automações e IA."),
            ("en", "Programming and Data", "Automation and AI."),
        ],
    )
    def test_hero_keeps_translated_content(self, client, language, title, accent):
        with override(language):
            html = client.get(reverse("core:home")).content.decode()
        hero = html.split('<section id="inicio"', 1)[1].split("</section>", 1)[0]

        assert title in hero
        assert accent in hero
        assert f"03 / {'AI' if language == 'en' else 'IA'}" in hero


@pytest.mark.django_db
class TestLegacyRedirects:
    """As URLs do site multipágina viram 301 para as âncoras da one-page."""

    @pytest.mark.parametrize(
        "url_name,anchor",
        [
            ("core:sobre", "#inicio"),
            ("core:competencias", "#habilidades"),
            ("core:projetos", "#projetos"),
            ("core:experiencias", "#experiencia"),
            ("core:formacao", "#formacao"),
            ("core:contato", "#contatos"),
        ],
    )
    def test_legacy_page_redirects_permanently(self, client: Client, url_name, anchor):
        response = client.get(reverse(url_name))
        assert response.status_code == 301
        assert response.url == reverse("core:home") + anchor


@pytest.mark.django_db
class TestContatoView:
    """Formulário de contato: POST em /contato/, renderizado na one-page."""

    @patch("apps.core.views.send_mail")
    def test_post_valid_saves_contact(self, mock_send_mail, client: Client):
        data = {
            "name": "João Silva",
            "email": "joao@email.com",
            "message": "Mensagem de teste",
        }
        response = client.post(reverse("core:contato"), data)
        assert response.status_code == 302
        assert Contact.objects.count() == 1
        contact = Contact.objects.first()
        assert contact.name == "João Silva"
        assert contact.email == "joao@email.com"

    @patch("apps.core.views.send_mail")
    def test_post_valid_sends_email(self, mock_send_mail, client: Client):
        data = {
            "name": "João Silva",
            "email": "joao@email.com",
            "message": "Mensagem de teste",
        }
        client.post(reverse("core:contato"), data)
        mock_send_mail.assert_called_once()
        call_kwargs = mock_send_mail.call_args
        assert "João Silva" in call_kwargs[1]["subject"]
        assert call_kwargs[1]["recipient_list"] == ["davioliveiraes7@gmail.com"]

    @patch("apps.core.views.send_mail")
    def test_post_valid_redirects_to_contact_section(
        self, mock_send_mail, client: Client
    ):
        data = {
            "name": "João Silva",
            "email": "joao@email.com",
            "message": "Mensagem de teste",
        }
        response = client.post(reverse("core:contato"), data)
        assert response.status_code == 302
        assert response.url == reverse("core:home") + "?sent=1#contatos"

    @patch("apps.core.views.send_mail")
    def test_sent_flag_shows_confirmation(self, mock_send_mail, client: Client):
        html = client.get(reverse("core:home") + "?sent=1").content.decode()
        assert "form-success" in html

    def test_post_invalid_does_not_save(self, client: Client):
        data = {"name": "", "email": "invalido", "message": ""}
        client.post(reverse("core:contato"), data)
        assert Contact.objects.count() == 0

    def test_post_invalid_rerenders_home_with_errors(self, client: Client):
        data = {"name": "", "email": "invalido", "message": ""}
        response = client.post(reverse("core:contato"), data)
        assert response.status_code == 200
        assert "core/home.html" in [t.name for t in response.templates]
        assert response.context["form"].errors
