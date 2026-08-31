# Encurta os textos dos cards com imagem para que caibam confortavelmente,
# preservando a descrição essencial e o ponto final.

from django.db import migrations

PROJECT_DESCRIPTIONS = {
    "Apex Acelera | Reports": {
        "description": (
            "Relatórios em PDF com dados do Meta Ads, quatro modos de análise e "
            "KPIs automáticos."
        ),
        "description_en": (
            "PDF reports from Meta Ads data, with four analysis modes and "
            "automated KPIs."
        ),
        "old_description": (
            "Gerador de relatórios em PDF para dados do Meta Ads, com quatro modos "
            "de análise e cálculo automático de KPIs."
        ),
        "old_description_en": (
            "PDF report generator for Meta Ads data, with four analysis modes and "
            "automatic KPI calculation."
        ),
    },
    "Ecommerce Control": {
        "description": (
            "Painel multi-tenant que integra Nuvemshop e GestãoClick para "
            "centralizar a operação."
        ),
        "description_en": (
            "Multi-tenant dashboard integrating Nuvemshop and GestãoClick into "
            "one operation."
        ),
        "old_description": (
            "Painel multi-tenant que integra Nuvemshop e GestãoClick para centralizar "
            "catálogo, financeiro e relatórios em PDF."
        ),
        "old_description_en": (
            "Multi-tenant dashboard integrating Nuvemshop and GestãoClick to "
            "centralize catalog, finance, and PDF reports."
        ),
    },
    "E-commerce Ibeize": {
        "description": (
            "E-commerce integrado ao GestãoClick, com GoTemplate, Melhor Envio e "
            "estoque sincronizado."
        ),
        "description_en": (
            "E-commerce integrated with GestãoClick, GoTemplate, Melhor Envio, and "
            "synchronized inventory."
        ),
        "old_description": (
            "E-commerce integrado ao GestãoClick, com storefront em GoTemplate, "
            "logística via Melhor Envio e estoque sincronizado."
        ),
        "old_description_en": (
            "E-commerce integrated with GestãoClick, featuring a GoTemplate "
            "storefront, Melhor Envio shipping, and synchronized inventory."
        ),
    },
    "Portfólio Pessoal": {
        "description": (
            "Portfólio bilíngue em Django, com temas claro e escuro, busca, contato "
            "e design responsivo."
        ),
        "description_en": (
            "Bilingual Django portfolio with light and dark themes, search, contact, "
            "and responsive design."
        ),
        "old_description": (
            "Portfólio profissional bilíngue em Django, com temas claro e escuro, "
            "busca rápida, contato e design responsivo."
        ),
        "old_description_en": (
            "Bilingual professional portfolio built with Django, featuring light and "
            "dark themes, quick search, contact form, and responsive design."
        ),
    },
}


def apply_descriptions(apps, schema_editor):
    Project = apps.get_model("core", "Project")
    for title, copy in PROJECT_DESCRIPTIONS.items():
        Project.objects.filter(title=title).update(
            description=copy["description"],
            description_en=copy["description_en"],
        )


def revert_descriptions(apps, schema_editor):
    Project = apps.get_model("core", "Project")
    for title, copy in PROJECT_DESCRIPTIONS.items():
        Project.objects.filter(title=title).update(
            description=copy["old_description"],
            description_en=copy["old_description_en"],
        )


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0023_refresh_project_previews"),
    ]

    operations = [
        migrations.RunPython(apply_descriptions, revert_descriptions),
    ]
