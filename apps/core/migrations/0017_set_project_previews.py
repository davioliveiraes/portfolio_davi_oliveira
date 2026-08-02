# Preenche o preview dos projetos que têm interface. Os demais (APIs, sem
# frontend) ficam com o campo vazio e o card renderiza a capa neutra.

from django.db import migrations

# título -> caminho dentro de static/
PREVIEWS = {
    "Apex Reports": "images/projects/apex-reports.webp",
    "Ecommerce Control": "images/projects/ecommerce-control.webp",
    "E-commerce Ibeize": "images/projects/ecommerce-ibeize.webp",
    "Portfólio Pessoal": "images/projects/portfolio-pessoal.webp",
}


def set_previews(apps, schema_editor):
    Project = apps.get_model("core", "Project")
    for title, path in PREVIEWS.items():
        Project.objects.filter(title=title).update(image=path)


def clear_previews(apps, schema_editor):
    Project = apps.get_model("core", "Project")
    Project.objects.filter(title__in=PREVIEWS).update(image="")


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0016_project_preview_image"),
    ]

    operations = [
        migrations.RunPython(set_previews, clear_previews),
    ]
