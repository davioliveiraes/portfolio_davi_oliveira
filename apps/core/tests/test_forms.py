import pytest

from apps.core.forms import ContactForm


class TestContactForm:
    def test_valid_form(self):
        form = ContactForm(
            data={
                "name": "João Silva",
                "email": "joao@email.com",
                "message": "Mensagem de teste",
            }
        )
        assert form.is_valid()

    def test_empty_name_invalid(self):
        form = ContactForm(
            data={"name": "", "email": "joao@email.com", "message": "Msg"}
        )
        assert not form.is_valid()
        assert "name" in form.errors

    def test_empty_email_invalid(self):
        form = ContactForm(data={"name": "João", "email": "", "message": "Msg"})
        assert not form.is_valid()
        assert "email" in form.errors

    def test_invalid_email_format(self):
        form = ContactForm(
            data={"name": "João", "email": "email-invalido", "message": "Msg"}
        )
        assert not form.is_valid()
        assert "email" in form.errors

    def test_empty_message_invalid(self):
        form = ContactForm(
            data={"name": "João", "email": "joao@email.com", "message": ""}
        )
        assert not form.is_valid()
        assert "message" in form.errors

    def test_all_fields_empty(self):
        form = ContactForm(data={})
        assert not form.is_valid()
        assert len(form.errors) == 3

    def test_widgets_have_placeholders(self):
        form = ContactForm()
        assert form.fields["name"].widget.attrs["placeholder"] == "Seu nome"
        assert form.fields["email"].widget.attrs["placeholder"] == "seu@email.com"
        assert "placeholder" in form.fields["message"].widget.attrs
