# Adiciona o projeto Ecommerce Control aos Projetos Técnicos.

from django.db import migrations
from django.db.models import Max


def add_project(apps, schema_editor):
    Project = apps.get_model("core", "Project")

    if Project.objects.filter(title="Ecommerce Control").exists():
        return

    last_order = Project.objects.aggregate(m=Max("order"))["m"] or 0
    Project.objects.create(
        category="tecnico",
        title="Ecommerce Control",
        title_en="Ecommerce Control",
        description=(
            "Painel de controle multi-tenant para lojistas Nuvemshop + GestãoClick "
            "— catálogo, financeiro e relatórios em PDF em um só lugar. Cada "
            "empresa cria sua conta e enxerga apenas os próprios dados."
        ),
        description_en=(
            "Multi-tenant control panel for Nuvemshop + GestãoClick merchants — "
            "catalog, finance and PDF reports in one place. Each company creates "
            "its own account and sees only its own data."
        ),
        tags="Django Ninja, React, TypeScript, PostgreSQL, Docker",
        github_url="https://github.com/davioliveiraes/ecommerce-control",
        live_url="",
        order=last_order + 1,
    )


def remove_project(apps, schema_editor):
    Project = apps.get_model("core", "Project")
    Project.objects.filter(title="Ecommerce Control").delete()


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_update_ibeize_experience"),
    ]

    operations = [
        migrations.RunPython(add_project, remove_project),
    ]
