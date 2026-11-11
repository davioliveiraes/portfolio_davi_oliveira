# Remove o Ecommerce Control, que saiu dos "Projetos selecionados" do
# currículo (curriculo.pdf atualizado em 2026-11-11). O repositório continua
# no GitHub.

from django.db import migrations

PROJECT = {
    "category": "tecnico",
    "title": "Ecommerce Control",
    "title_en": "Ecommerce Control",
    "description": "Painel multi-tenant para lojistas NuvemShop e GestãoClick.",
    "description_en": "Multi-tenant dashboard for NuvemShop and GestãoClick merchants.",
    "tags": "Django Ninja, PostgreSQL, React, Docker",
    "tags_en": "",
    "github_url": "https://github.com/davioliveiraes/ecommerce-control",
    "live_url": "",
    "image": "images/projects/ecommerce-control.webp",
    "order": 5,
}


def apply_content(apps, schema_editor):
    Project = apps.get_model("core", "Project")
    Project.objects.using(schema_editor.connection.alias).filter(
        github_url=PROJECT["github_url"]
    ).delete()


def restore_content(apps, schema_editor):
    Project = apps.get_model("core", "Project")
    Project.objects.using(schema_editor.connection.alias).get_or_create(
        github_url=PROJECT["github_url"], defaults=PROJECT
    )


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0030_curate_projects"),
    ]

    operations = [
        migrations.RunPython(apply_content, restore_content),
    ]
