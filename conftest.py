import pytest


@pytest.fixture
def client():
    """Fixture para o cliente de teste do Django."""
    from django.test import Client

    return Client()


@pytest.fixture(autouse=True)
def no_github_api(monkeypatch):
    """Evita chamadas reais à API do GitHub nas views durante os testes."""
    monkeypatch.setattr("apps.core.views.get_github_repos", lambda: {})
