import pytest


@pytest.fixture
def client():
    """Fixture para o cliente de teste do Django."""
    from django.test import Client

    return Client()
