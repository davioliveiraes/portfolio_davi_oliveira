# Reordena os projetos do mais novo ao mais velho, pela data de criação do
# repositório no GitHub (Ibeize, sem repo, entra em fev/2026 — início do
# trabalho conforme a experiência na iBeize).

from django.db import migrations

# título -> (ordem nova, ordem antiga)
ORDERS = {
    "Ecommerce Control": (0, 11),  # 2026-06-06
    "Portfólio Pessoal": (1, 7),  # 2026-03-29 23:58
    "API de Pedidos com JWT": (2, 6),  # 2026-03-29 23:44
    "API Bancária Segura com JWT": (3, 5),  # 2026-03-25
    "E-commerce Ibeize": (4, 10),  # fev/2026
    "API de Sistema Bancário": (5, 1),  # 2025-12-11
    "API de Adoção de Pets": (6, 3),  # 2025-11-15
    "API Encurtador de Links": (7, 0),  # 2025-08-24
    "Chat em Tempo Real": (8, 4),  # 2025-08-07
    "Projetos de Ciência de Dados": (9, 9),  # 2025-07-08
    "API Dieta Diária": (10, 2),  # 2025-06-30
    "Projetos Python": (11, 8),  # 2024-03-11
}


def apply_orders(apps, schema_editor, index):
    Project = apps.get_model("core", "Project")
    for title, orders in ORDERS.items():
        Project.objects.filter(title=title).update(order=orders[index])


def reorder(apps, schema_editor):
    apply_orders(apps, schema_editor, 0)


def restore(apps, schema_editor):
    apply_orders(apps, schema_editor, 1)


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0009_add_ecommerce_control_project"),
    ]

    operations = [
        migrations.RunPython(reorder, restore),
    ]
