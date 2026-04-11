import pytest

from apps.core.models import Contact


@pytest.mark.django_db
class TestContactModel:
    def test_create_contact(self):
        contact = Contact.objects.create(
            name="João Silva",
            email="joao@email.com",
            message="Mensagem de teste",
        )
        assert contact.pk is not None
        assert contact.read is False

    def test_str_representation(self):
        contact = Contact(name="João Silva", email="joao@email.com")
        assert str(contact) == "João Silva - joao@email.com"

    def test_ordering_newest_first(self):
        c1 = Contact.objects.create(name="Primeiro", email="a@email.com", message="msg")
        c2 = Contact.objects.create(name="Segundo", email="b@email.com", message="msg")
        contacts = list(Contact.objects.all())
        assert contacts[0] == c2
        assert contacts[1] == c1

    def test_verbose_names(self):
        assert Contact._meta.verbose_name == "Mensagem"
        assert Contact._meta.verbose_name_plural == "Mensagens"
