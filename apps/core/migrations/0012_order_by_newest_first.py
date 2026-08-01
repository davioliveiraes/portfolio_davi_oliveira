# Projetos e certificações passam a listar o cadastro mais recente primeiro.
# O campo "order" vira destaque manual (maior primeiro) e é zerado, para que a
# ordenação padrão seja só a de cadastro.

from django.db import migrations, models

# título -> ordem anterior (ordem curada por data de repositório, da migration 0010)
PROJECT_ORDERS = {
    "Ecommerce Control": 0,
    "Portfólio Pessoal": 1,
    "API de Pedidos com JWT": 2,
    "API Bancária Segura com JWT": 3,
    "E-commerce Ibeize": 4,
    "API de Sistema Bancário": 5,
    "API de Adoção de Pets": 6,
    "API Encurtador de Links": 7,
    "Chat em Tempo Real": 8,
    "Projetos de Ciência de Dados": 9,
    "API Dieta Diária": 10,
    "Projetos Python": 11,
}

# nome -> ordem anterior
CERTIFICATION_ORDERS = {
    "Arquitetura de Software e Padrão MVC": 0,
    "Design do Código: SOLID e Testes": 1,
    "Explorando Flask": 2,
    "Fundamentos de Python": 3,
    "Python 3 Completo": 4,
    "Imersão Build & Automate: desenvolvimento e automação com IA": 5,
    "Logic Master: lógica de programação e algoritmos com Python": 6,
    "Autenticação JWT e Segurança": 7,
}


def clear_orders(apps, schema_editor):
    apps.get_model("core", "Project").objects.update(order=0)
    apps.get_model("core", "Certification").objects.update(order=0)


def restore_orders(apps, schema_editor):
    Project = apps.get_model("core", "Project")
    for title, order in PROJECT_ORDERS.items():
        Project.objects.filter(title=title).update(order=order)

    Certification = apps.get_model("core", "Certification")
    for name, order in CERTIFICATION_ORDERS.items():
        Certification.objects.filter(name=name).update(order=order)


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0011_redesign_copy_and_skills"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="project",
            options={
                "ordering": ["-order", "-id"],
                "verbose_name": "Projeto",
                "verbose_name_plural": "Projetos",
            },
        ),
        migrations.AlterModelOptions(
            name="certification",
            options={
                "ordering": ["-order", "-id"],
                "verbose_name": "Certificação",
                "verbose_name_plural": "Certificações",
            },
        ),
        migrations.AlterField(
            model_name="project",
            name="order",
            field=models.PositiveSmallIntegerField(
                default=0,
                help_text="Maior valor aparece primeiro. Deixe 0 para seguir a "
                "ordem de cadastro (o mais recente primeiro).",
                verbose_name="Destaque",
            ),
        ),
        migrations.AlterField(
            model_name="certification",
            name="order",
            field=models.PositiveSmallIntegerField(
                default=0,
                help_text="Maior valor aparece primeiro. Deixe 0 para seguir a "
                "ordem de cadastro (a mais recente primeiro).",
                verbose_name="Destaque",
            ),
        ),
        migrations.RunPython(clear_orders, restore_orders),
    ]
