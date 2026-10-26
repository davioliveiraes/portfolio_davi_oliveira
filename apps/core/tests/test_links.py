from django.urls import reverse

import pytest

from apps.core.links import HubLink, get_hub_links


@pytest.mark.django_db
class TestHubLinks:
    def test_returns_curriculo_link(self):
        links = get_hub_links()
        assert len(links) == 1
        assert isinstance(links[0], HubLink)
        assert links[0].url == reverse("core:curriculo")
        assert links[0].title == "Currículo"
