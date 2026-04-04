from django.test import Client
from django.urls import reverse

import pytest


@pytest.mark.django_db
class TestHomeView:
    def test_home_status_code(self, client: Client):
        response = client.get(reverse("core:home"))
        assert response.status_code == 200

    def test_home_template_used(self, client: Client):
        response = client.get(reverse("core:home"))
        assert "core/home.html" in [t.name for t in response.templates]
