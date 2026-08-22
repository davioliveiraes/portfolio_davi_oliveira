# Ajusta o cargo na Apex Acelera para refletir o foco em Dados.

from django.db import migrations

COMPANY = "Apex Acelera"

NEW_ROLE = "Gestor de Dados e Automação com IA"
NEW_ROLE_EN = "Data and AI Automation Manager"

OLD_ROLE = "Analista de Growth e Automação com IA"
OLD_ROLE_EN = "Growth and AI Automation Analyst"


def apply_role(apps, schema_editor):
    Experience = apps.get_model("core", "Experience")
    Experience.objects.filter(company=COMPANY).update(
        role=NEW_ROLE,
        role_en=NEW_ROLE_EN,
    )


def revert_role(apps, schema_editor):
    Experience = apps.get_model("core", "Experience")
    Experience.objects.filter(company=COMPANY).update(
        role=OLD_ROLE,
        role_en=OLD_ROLE_EN,
    )


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0021_backend_and_data_focus"),
    ]

    operations = [
        migrations.RunPython(apply_role, revert_role),
    ]
