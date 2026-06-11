import logging

from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils.translation import gettext as _

from .forms import ContactForm

logger = logging.getLogger(__name__)


def robots_txt(request):
    sitemap_url = request.build_absolute_uri("/sitemap.xml")
    content = f"User-agent: *\nAllow: /\nDisallow: /admin/\n\nSitemap: {sitemap_url}\n"
    return HttpResponse(content, content_type="text/plain")


def home(request):
    return render(request, "core/home.html")


def sobre(request):
    return render(request, "core/sobre.html")


def competencias(request):
    return render(request, "core/competencias.html")


def projetos(request):
    return render(request, "core/projetos.html")


def experiencias(request):
    return render(request, "core/experiencias.html")


def formacao(request):
    return render(request, "core/formacao.html")


def contato(request):
    if request.method == "POST":
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
            messages.success(
                request, _("Mensagem enviada com sucesso! Obrigado pelo contato.")
            )
            return redirect("core:contato")
        else:
            messages.error(
                request, _("Erro ao enviar. Verifique os campos e tente novamente.")
            )
    else:
        form = ContactForm()
    return render(request, "core/contato.html", {"form": form})
