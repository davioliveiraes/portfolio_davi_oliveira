# Adiciona o micro-certificado "NoSQL com MongoDB" da Rocketseat (16/09/2026).

from django.db import migrations

NAME = "NoSQL com MongoDB"
NAME_EN = "NoSQL with MongoDB"
INSTITUTION = "Rocketseat"
HOURS = 6


def add_certification(apps, schema_editor):
    Certification = apps.get_model("core", "Certification")
    Certification.objects.get_or_create(
        name=NAME,
        institution=INSTITUTION,
        defaults={"name_en": NAME_EN, "hours": HOURS},
    )


def remove_certification(apps, schema_editor):
    Certification = apps.get_model("core", "Certification")
    Certification.objects.filter(name=NAME, institution=INSTITUTION).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0025_refresh_experience_details_and_apex_image"),
    ]

    operations = [
        migrations.RunPython(add_certification, remove_certification),
    ]
