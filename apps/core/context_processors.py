"""Context processors do app core."""

from urllib.parse import urlparse

from django.conf import settings
from django.http import HttpRequest


def site_meta(request: HttpRequest) -> dict[str, str]:
    """Expõe o domínio do site em todos os templates, a partir de
    settings.SITE_URL (uma única variável de ambiente)."""
    site_url: str = settings.SITE_URL
    return {
        "SITE_URL": site_url,
        "SITE_DOMAIN": urlparse(site_url).netloc,
    }
