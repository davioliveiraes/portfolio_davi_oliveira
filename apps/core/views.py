import logging

from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils.translation import gettext as _

from .forms import ContactForm
from .models import Certification, Experience, Project, Skill, SkillCategory
from .services import get_github_repos

logger = logging.getLogger(__name__)


def robots_txt(request):
    sitemap_url = request.build_absolute_uri("/sitemap.xml")
    content = f"User-agent: *\nAllow: /\nDisallow: /admin/\n\nSitemap: {sitemap_url}\n"
    return HttpResponse(content, content_type="text/plain")


def home(request):
    stats = {
        "projects": Project.objects.count(),
        "github_repos": len(get_github_repos()),
        "certifications": Certification.objects.count(),
        "skills": Skill.objects.count(),
    }
    return render(request, "core/home.html", {"stats": stats})


def sobre(request):
    return render(request, "core/sobre.html")


def competencias(request):
    categories = SkillCategory.objects.prefetch_related("skills")
    return render(request, "core/competencias.html", {"categories": categories})


def projetos(request):
    projects = list(Project.objects.all())

    github_repos = get_github_repos()
    for project in projects:
        project.github = github_repos.get(project.repo_name)

    # Filtros curados: label exibido + palavras-chave (separadas por |)
    # comparadas, sem case, contra as tags de cada projeto.
    filters = [
        {"label": "Python", "keywords": "python"},
        {"label": "Django", "keywords": "django"},
        {"label": "FastAPI", "keywords": "fastapi"},
        {"label": "Flask", "keywords": "flask"},
        {"label": "GoLang", "keywords": "golang"},
        {"label": "PostgreSQL", "keywords": "postgresql"},
        {"label": "SQLite", "keywords": "sqlite"},
        {"label": "Pytest", "keywords": "pytest"},
        {"label": "PyJWT", "keywords": "pyjwt"},
        {"label": "Bcrypt", "keywords": "bcrypt"},
        {"label": _("Dados"), "keywords": "pandas|scikit|tensorflow|jupyter|numpy"},
    ]

    return render(
        request,
        "core/projetos.html",
        {"projects": projects, "filters": filters},
    )


def experiencias(request):
    experiences = Experience.objects.all()
    return render(request, "core/experiencias.html", {"experiences": experiences})


def formacao(request):
    certifications = Certification.objects.all()
    return render(request, "core/formacao.html", {"certifications": certifications})


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
