import logging
from dataclasses import dataclass
from urllib.parse import urlparse

from django.conf import settings
from django.contrib.sitemaps.views import x_robots_tag
from django.core.mail import EmailMessage
from django.core.paginator import EmptyPage, PageNotAnInteger
from django.http import (
    Http404,
    HttpRequest,
    HttpResponse,
    HttpResponsePermanentRedirect,
)
from django.shortcuts import redirect, render
from django.template.response import TemplateResponse
from django.urls import reverse

from .forms import ContactForm
from .links import get_hub_links
from .models import Certification, Experience, Project, SkillCategory

logger = logging.getLogger(__name__)


def robots_txt(request: HttpRequest) -> HttpResponse:
    sitemap_url = f"{settings.SITE_URL}/sitemap.xml"
    content = f"User-agent: *\nAllow: /\nDisallow: /admin/\n\nSitemap: {sitemap_url}\n"
    return HttpResponse(content, content_type="text/plain")


@dataclass
class _FixedDomainSite:
    """Substitui django.contrib.sites.Site/RequestSite só para dar domínio
    (settings.SITE_DOMAIN) aos sitemaps, sem envolver o Host da requisição
    nem exigir o app django.contrib.sites."""

    domain: str


@x_robots_tag
def sitemap_view(
    request: HttpRequest, sitemaps: dict, section: str | None = None
) -> TemplateResponse:
    """Equivalente a django.contrib.sitemaps.views.sitemap, mas com domínio
    fixo em SITE_URL em vez do Host da requisição — o sitemap é conteúdo
    público indexado por buscadores e não deve variar conforme quem pediu."""
    site = _FixedDomainSite(domain=urlparse(settings.SITE_URL).netloc)
    protocol = request.scheme
    if section is not None:
        if section not in sitemaps:
            raise Http404(f"No sitemap available for section: {section!r}")
        maps = [sitemaps[section]]
    else:
        maps = list(sitemaps.values())
    page = request.GET.get("p", 1)

    urls = []
    try:
        for sitemap in maps:
            if callable(sitemap):
                sitemap = sitemap()
            urls.extend(sitemap.get_urls(page=page, site=site, protocol=protocol))
    except EmptyPage:
        raise Http404(f"Page {page} empty")
    except PageNotAnInteger:
        raise Http404(f"No page {page!r}")

    return TemplateResponse(
        request, "sitemap.xml", {"urlset": urls}, content_type="application/xml"
    )


def _home_context(form=None):
    """Contexto completo da one-page (todas as seções em uma renderização)."""
    return {
        "experiences": Experience.objects.all(),
        "categories": SkillCategory.objects.prefetch_related("skills"),
        "projects": Project.objects.all(),
        "filters": [
            {"label": label, "value": value}
            for value, label in Project.Category.choices
        ],
        "certifications": Certification.objects.all(),
        "form": form or ContactForm(),
        # Diz ao base.html que a nav deve usar âncoras internas (não links
        # para /curriculo): só esta página tem as seções de fato.
        "is_curriculo": True,
    }


def home(request):
    """Hub pessoal minimalista (link-in-bio). Conteúdo completo mora em /curriculo."""
    return render(request, "core/home.html", {"links": get_hub_links()})


def curriculo(request):
    context = _home_context()
    context["contact_sent"] = request.GET.get("sent") == "1"
    return render(request, "core/curriculo.html", context)


def _redirect_to_section(section):
    """As URLs antigas do site multipágina viram 301 para as âncoras do /curriculo."""

    def view(request):
        return HttpResponsePermanentRedirect(reverse("core:curriculo") + f"#{section}")

    return view


sobre = _redirect_to_section("inicio")
competencias = _redirect_to_section("habilidades")
projetos = _redirect_to_section("projetos")
experiencias = _redirect_to_section("experiencia")
formacao = _redirect_to_section("formacao")


def contato(request):
    if request.method != "POST":
        return HttpResponsePermanentRedirect(reverse("core:curriculo") + "#contatos")

    form = ContactForm(request.POST)
    if form.is_valid():
        if form.is_spam():
            # Bot caiu no honeypot: responde como sucesso, sem salvar nem notificar
            return redirect(reverse("core:curriculo") + "?sent=1#contatos")
        form.save()
        try:
            EmailMessage(
                subject=f"[Portfólio] Nova mensagem de {form.cleaned_data['name']}",
                body=f"Nome: {form.cleaned_data['name']}\n"
                f"Email: {form.cleaned_data['email']}\n\n"
                f"{form.cleaned_data['message']}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.CONTACT_EMAIL],
                # "Responder" no cliente de email vai direto para o visitante
                reply_to=[form.cleaned_data["email"]],
            ).send(fail_silently=False)
        except Exception:
            # A mensagem já está salva no banco; falha no SMTP não deve
            # quebrar a experiência do visitante.
            logger.exception("Falha ao enviar email de notificação de contato")
        return redirect(reverse("core:curriculo") + "?sent=1#contatos")

    # Formulário inválido: re-renderiza o currículo com os erros de campo
    return render(request, "core/curriculo.html", _home_context(form=form))
