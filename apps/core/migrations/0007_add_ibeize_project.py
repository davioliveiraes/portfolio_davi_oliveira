# Torna a URL do GitHub opcional (projetos de clientes não têm repositório
# público) e adiciona o e-commerce da Ibeize em Soluções Empresariais.

from django.db import migrations, models
from django.db.models import Max


def add_ibeize(apps, schema_editor):
    Project = apps.get_model("core", "Project")

    if Project.objects.filter(title="E-commerce Ibeize").exists():
        return

    last_order = Project.objects.aggregate(m=Max("order"))["m"] or 0
    Project.objects.create(
        category="empresarial",
        title="E-commerce Ibeize",
        title_en="Ibeize E-commerce",
        description=(
            "Customização do storefront via CSS/HTML/JS/GoTemplate avançado e "
            "integração com ERP GestãoClick. Análise de resultados, experimentação "
            "e otimizações contínuas da loja NuvemShop. Configuração de DNS, "
            "integração com Melhor Envio e alinhamento de SKUs com estoque."
        ),
        description_en=(
            "Storefront customization with advanced CSS/HTML/JS/GoTemplate and "
            "integration with the GestãoClick ERP. Results analysis, "
            "experimentation and continuous optimizations of the NuvemShop store. "
            "DNS setup, Melhor Envio shipping integration and SKU alignment with "
            "inventory."
        ),
        tags="NuvemShop, GoTemplate, JavaScript, GestãoClick",
        github_url="",
        live_url="https://ibeize.com.br",
        order=last_order + 1,
    )


def remove_ibeize(apps, schema_editor):
    Project = apps.get_model("core", "Project")
    Project.objects.filter(title="E-commerce Ibeize").delete()


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_project_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="github_url",
            field=models.URLField(blank=True, verbose_name="URL do GitHub"),
        ),
        migrations.RunPython(add_ibeize, remove_ibeize),
    ]
