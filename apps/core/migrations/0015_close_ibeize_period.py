# Encerramento do trabalho na iBeize: Jul 2026.

from django.db import migrations

NEW_PT = "Fev 2026 a Jul 2026 · Morada Nova, CE"
NEW_EN = "Feb 2026 to Jul 2026 · Morada Nova, CE"
OLD_PT = "Fev 2026 até hoje · Morada Nova, CE"
OLD_EN = "Feb 2026 to today · Morada Nova, CE"


def set_period(apps, period, period_en):
    Experience = apps.get_model("core", "Experience")
    Experience.objects.filter(company="iBeize").update(
        period=period, period_en=period_en
    )


def close_period(apps, schema_editor):
    set_period(apps, NEW_PT, NEW_EN)


def reopen_period(apps, schema_editor):
    set_period(apps, OLD_PT, OLD_EN)


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0014_add_apex_reports_project"),
    ]

    operations = [
        migrations.RunPython(close_period, reopen_period),
    ]
