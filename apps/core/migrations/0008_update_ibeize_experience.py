# Enxuga as atividades da experiência na iBeize para quatro pontos.

from django.db import migrations

NEW_DETAILS = (
    "Análise de resultados, experimentação e otimizações contínuas da loja NuvemShop\n"
    "Customização do storefront via CSS/HTML/JS/GoTemplate avançado e integração com ERP GestãoClick\n"
    "Configuração de DNS, integração com Melhor Envio e alinhamento de SKUs com estoque\n"
    "Suporte em ações comerciais e integração com operação logística"
)

NEW_DETAILS_EN = (
    "Results analysis, experimentation, and continuous optimizations for the NuvemShop store\n"
    "Storefront customization via advanced CSS/HTML/JS/GoTemplate and integration with GestãoClick ERP\n"
    "DNS configuration, integration with Melhor Envio, and SKU alignment with inventory\n"
    "Support for commercial actions and integration with logistics operations"
)

OLD_DETAILS = (
    "Análise de resultados, experimentação e otimizações contínuas da loja NuvemShop\n"
    "Customização do storefront via CSS/HTML/JS/GoTemplate avançado e integração com ERP GestãoClick\n"
    "Monitoramento de KPIs, testes de performance e otimização de ROI\n"
    "Configuração de DNS, integração com Melhor Envio e alinhamento de SKUs com estoque\n"
    "Desenvolvimento do Ibeize Ecommerce Control — sistema interno fullstack (Django Ninja + React + Docker) para gestão de catálogo e finanças\n"
    "Suporte em ações comerciais e integração com operação logística"
)

OLD_DETAILS_EN = (
    "Results analysis, experimentation, and continuous optimizations for the NuvemShop store\n"
    "Storefront customization via advanced CSS/HTML/JS/GoTemplate and integration with GestãoClick ERP\n"
    "KPI monitoring, performance testing, and ROI optimization\n"
    "DNS configuration, integration with Melhor Envio, and SKU alignment with inventory\n"
    "Development of Ibeize Ecommerce Control — internal fullstack system (Django Ninja + React + Docker) for catalog and finance management\n"
    "Support for commercial actions and integration with logistics operations"
)


def update_details(apps, schema_editor):
    Experience = apps.get_model("core", "Experience")
    Experience.objects.filter(company="iBeize").update(
        details=NEW_DETAILS, details_en=NEW_DETAILS_EN
    )


def restore_details(apps, schema_editor):
    Experience = apps.get_model("core", "Experience")
    Experience.objects.filter(company="iBeize").update(
        details=OLD_DETAILS, details_en=OLD_DETAILS_EN
    )


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_add_ibeize_project"),
    ]

    operations = [
        migrations.RunPython(update_details, restore_details),
    ]
