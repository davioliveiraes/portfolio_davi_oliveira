# Adiciona o projeto Apex Reports às Soluções Empresariais.

from django.db import migrations


def add_project(apps, schema_editor):
    Project = apps.get_model("core", "Project")

    if Project.objects.filter(title="Apex Reports").exists():
        return

    Project.objects.create(
        category="empresarial",
        title="Apex Reports",
        title_en="Apex Reports",
        description=(
            "Gerador de relatórios em PDF a partir de exports do Meta Ads "
            "Manager, com quatro modos de saída, cálculo de KPIs e deploy em "
            "VPS (Nginx, Gunicorn, systemd)."
        ),
        description_en=(
            "PDF report generator built from Meta Ads Manager exports, with "
            "four output modes, KPI calculation and VPS deploy (Nginx, "
            "Gunicorn, systemd)."
        ),
        tags="Django, PostgreSQL, WeasyPrint",
        github_url="https://github.com/davioliveiraes/apex-reports",
        live_url="",
        order=0,
    )


def remove_project(apps, schema_editor):
    Project = apps.get_model("core", "Project")
    Project.objects.filter(title="Apex Reports").delete()


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0013_recategorize_projects"),
    ]

    operations = [
        migrations.RunPython(add_project, remove_project),
    ]
