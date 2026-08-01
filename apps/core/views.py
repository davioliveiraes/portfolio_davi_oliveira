import logging

from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import ContactForm
from .models import Certification, Experience, Project, SkillCategory

logger = logging.getLogger(__name__)


def robots_txt(request):
    sitemap_url = request.build_absolute_uri("/sitemap.xml")
    content = f"User-agent: *\nAllow: /\nDisallow: /admin/\n\nSitemap: {sitemap_url}\n"
    return HttpResponse(content, content_type="text/plain")


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
    }


def home(request):
    context = _home_context()
    context["contact_sent"] = request.GET.get("sent") == "1"
    return render(request, "core/home.html", context)


def _redirect_to_section(section):
    """As URLs antigas do site multipágina viram 301 para as âncoras."""

    def view(request):
        return HttpResponsePermanentRedirect(reverse("core:home") + f"#{section}")

    return view


sobre = _redirect_to_section("inicio")
competencias = _redirect_to_section("habilidades")
projetos = _redirect_to_section("projetos")
experiencias = _redirect_to_section("experiencia")
formacao = _redirect_to_section("formacao")


def contato(request):
    if request.method != "POST":
        return HttpResponsePermanentRedirect(reverse("core:home") + "#contatos")

    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        try:
            send_mail(
                subject=f"[Portfólio] Nova mensagem de {form.cleaned_data['name']}",
                message=f"Nome: {form.cleaned_data['name']}\n"
                f"Email: {form.cleaned_data['email']}\n\n"
                f"{form.cleaned_data['message']}",
                from_email="davioliveiraes7@gmail.com",
                recipient_list=["davioliveiraes7@gmail.com"],
                fail_silently=False,
            )
        except Exception:
            # A mensagem já está salva no banco; falha no SMTP não deve
            # quebrar a experiência do visitante.
            logger.exception("Falha ao enviar email de notificação de contato")
        return redirect(reverse("core:home") + "?sent=1#contatos")

    # Formulário inválido: re-renderiza a one-page com os erros de campo
    return render(request, "core/home.html", _home_context(form=form))
