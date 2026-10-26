"""Cards exibidos no hub pessoal ("/"). Adicionar um novo card é só acrescentar
uma HubLink aqui — o template (core/home.html) itera a lista, sem precisar
ser alterado."""

from dataclasses import dataclass

from django.urls import reverse
from django.utils.translation import gettext as _


@dataclass(frozen=True)
class HubLink:
    title: str
    subtitle: str
    url: str


def get_hub_links() -> list[HubLink]:
    """Chamada por request (não um literal de módulo): assim `_()` resolve no
    idioma ativo e `reverse()` roda dentro do ciclo normal de resolução de URL."""
    return [
        HubLink(
            title=_("Currículo"),
            subtitle=_("Experiência, projetos e formação"),
            url=reverse("core:curriculo"),
        ),
    ]
