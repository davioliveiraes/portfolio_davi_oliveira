from unittest.mock import patch

from django.test import Client
from django.urls import reverse

import pytest

from apps.core.models import Contact


@pytest.mark.django_db
class TestStaticPages:
    """Testa todas as páginas estáticas do portfólio."""

    @pytest.mark.parametrize(
        "url_name,template",
        [
            ("core:home", "core/home.html"),
            ("core:sobre", "core/sobre.html"),
            ("core:competencias", "core/competencias.html"),
            ("core:projetos", "core/projetos.html"),
            ("core:experiencias", "core/experiencias.html"),
            ("core:formacao", "core/formacao.html"),
            ("core:contato", "core/contato.html"),
        ],
    )
    def test_page_returns_200(self, client: Client, url_name, template):
        response = client.get(reverse(url_name))
        assert response.status_code == 200

    @pytest.mark.parametrize(
        "url_name,template",
        [
            ("core:home", "core/home.html"),
            ("core:sobre", "core/sobre.html"),
            ("core:competencias", "core/competencias.html"),
            ("core:projetos", "core/projetos.html"),
            ("core:experiencias", "core/experiencias.html"),
            ("core:formacao", "core/formacao.html"),
            ("core:contato", "core/contato.html"),
        ],
    )
    def test_page_uses_correct_template(self, client: Client, url_name, template):
        response = client.get(reverse(url_name))
        assert template in [t.name for t in response.templates]

    @pytest.mark.parametrize(
        "url_name",
        [
            "core:home",
            "core:sobre",
            "core:competencias",
            "core:projetos",
            "core:experiencias",
            "core:formacao",
            "core:contato",
        ],
    )
    def test_page_extends_base_template(self, client: Client, url_name):
        response = client.get(reverse(url_name))
        assert "base.html" in [t.name for t in response.templates]


@pytest.mark.django_db
class TestContatoView:
    """Testa o formulário de contato (GET e POST)."""

    def test_get_contains_form(self, client: Client):
        response = client.get(reverse("core:contato"))
        assert "form" in response.context

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
    def test_post_valid_redirects(self, mock_send_mail, client: Client):
        data = {
            "name": "João Silva",
            "email": "joao@email.com",
            "message": "Mensagem de teste",
        }
        response = client.post(reverse("core:contato"), data)
        assert response.status_code == 302
        assert response.url == reverse("core:contato")

    @patch("apps.core.views.send_mail")
    def test_post_valid_shows_success_message(self, mock_send_mail, client: Client):
        data = {
            "name": "João Silva",
            "email": "joao@email.com",
            "message": "Mensagem de teste",
        }
        response = client.post(reverse("core:contato"), data, follow=True)
        messages = list(response.context["messages"])
        assert len(messages) == 1
        assert "sucesso" in str(messages[0]).lower()

    def test_post_invalid_does_not_save(self, client: Client):
        data = {"name": "", "email": "invalido", "message": ""}
        client.post(reverse("core:contato"), data)
        assert Contact.objects.count() == 0

    def test_post_invalid_shows_error_message(self, client: Client):
        data = {"name": "", "email": "", "message": ""}
        response = client.post(reverse("core:contato"), data)
        messages = list(response.context["messages"])
        assert len(messages) == 1
        assert "erro" in str(messages[0]).lower()

    def test_post_invalid_returns_form_with_errors(self, client: Client):
        data = {"name": "", "email": "invalido", "message": ""}
        response = client.post(reverse("core:contato"), data)
        assert response.status_code == 200
        assert response.context["form"].errors
