# Adiciona TypeScript à categoria Frontend, entre JavaScript e React.js.

from django.db import migrations
from django.db.models import F


def add_typescript(apps, schema_editor):
    SkillCategory = apps.get_model("core", "SkillCategory")
    Skill = apps.get_model("core", "Skill")

    category = SkillCategory.objects.filter(name="Frontend").first()
    if category is None or category.skills.filter(name="TypeScript").exists():
        return

    # Abre espaço depois do JavaScript (order=0) e insere na sequência
    category.skills.filter(order__gte=1).update(order=F("order") + 1)
    Skill.objects.create(
        category=category,
        name="TypeScript",
        name_en="",
        detail="",
        detail_en="",
        icon="icon-ts",
        order=1,
    )


def remove_typescript(apps, schema_editor):
    Skill = apps.get_model("core", "Skill")
    Skill.objects.filter(name="TypeScript", category__name="Frontend").delete()


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_seed_portfolio_content"),
    ]

    operations = [
        migrations.RunPython(add_typescript, remove_typescript),
    ]
