# Alinha o cargo na Apex Acelera ao currículo (curriculo.pdf atualizado em
# 2026-11-11), que traz "Gestor de Dados e Tráfego Pago".

from django.db import migrations

COMPANY = "Apex Acelera"

NEW_ROLE = "Gestor de Dados e Tráfego Pago"
NEW_ROLE_EN = "Data and Paid Traffic Manager"

OLD_ROLE = "Gestor de Dados e Automação com IA"
OLD_ROLE_EN = "Data and AI Automation Manager"


def apply_role(apps, schema_editor):
    Experience = apps.get_model("core", "Experience")
    Experience.objects.using(schema_editor.connection.alias).filter(
        company=COMPANY, role=OLD_ROLE
    ).update(role=NEW_ROLE, role_en=NEW_ROLE_EN)


def revert_role(apps, schema_editor):
    Experience = apps.get_model("core", "Experience")
    Experience.objects.using(schema_editor.connection.alias).filter(
        company=COMPANY, role=NEW_ROLE
    ).update(role=OLD_ROLE, role_en=OLD_ROLE_EN)


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0032_split_hiper_experience"),
    ]

    operations = [
        migrations.RunPython(apply_role, revert_role),
    ]
