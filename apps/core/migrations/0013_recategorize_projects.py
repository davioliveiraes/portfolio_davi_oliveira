# Ecommerce Control passa a ser Solução Empresarial e o Portfólio Pessoal
# passa a ser Site & Landing Page.

from django.db import migrations

# título -> (categoria nova, categoria antiga)
CATEGORIES = {
    "Ecommerce Control": ("empresarial", "tecnico"),
    "Portfólio Pessoal": ("sites", "tecnico"),
}


def apply_categories(apps, index):
    Project = apps.get_model("core", "Project")
    for title, categories in CATEGORIES.items():
        Project.objects.filter(title=title).update(category=categories[index])


def recategorize(apps, schema_editor):
    apply_categories(apps, 0)


def restore(apps, schema_editor):
    apply_categories(apps, 1)


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0012_order_by_newest_first"),
    ]

    operations = [
        migrations.RunPython(recategorize, restore),
    ]
