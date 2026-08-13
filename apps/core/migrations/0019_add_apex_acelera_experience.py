# Entrada na Apex Acelera (Ago 2026), a experiência atual.
# Experience é ordenada por "order" crescente, que não aceita negativo: para o
# cargo novo nascer no topo, as experiências existentes descem uma posição.

from django.db import migrations
from django.db.models import F

COMPANY = "Apex Acelera"

ROLE = "Analista de Growth e Automação com IA"
ROLE_EN = "Growth and AI Automation Analyst"

PERIOD = "Ago 2026 até hoje · Remoto"
PERIOD_EN = "Aug 2026 to today · Remote"

DETAILS = (
    "Responsável pelos dois principais serviços da agência: "
    "Tráfego Pago e CRM com Agente de IA\n"
    "Estruturação e gestão de campanhas de tráfego pago, com acompanhamento de "
    "CAC, ROAS e otimização contínua de criativos e segmentação\n"
    "Implantação de CRM e construção de agentes de IA para qualificação e "
    "atendimento automatizado de leads\n"
    "Integração entre plataformas de anúncio, CRM e canais de atendimento, "
    "com automação de funil e relatórios"
)

DETAILS_EN = (
    "Responsible for the agency's two main services: "
    "Paid Traffic and CRM with an AI Agent\n"
    "Structuring and managing paid traffic campaigns, tracking CAC and ROAS "
    "with continuous optimization of creatives and targeting\n"
    "CRM rollout and development of AI agents for automated lead "
    "qualification and support\n"
    "Integration between ad platforms, CRM, and support channels, with funnel "
    "automation and reporting"
)

SKILLS = (
    "Meta Ads, CRM, Agentes de IA, Python, APIs, Automação, CAC, ROAS, "
    "Funil de Vendas"
)

SKILLS_EN = (
    "Meta Ads, CRM, AI Agents, Python, APIs, Automation, CAC, ROAS, Sales Funnel"
)


def add_experience(apps, schema_editor):
    Experience = apps.get_model("core", "Experience")
    Experience.objects.update(order=F("order") + 1)
    Experience.objects.create(
        role=ROLE,
        role_en=ROLE_EN,
        company=COMPANY,
        period=PERIOD,
        period_en=PERIOD_EN,
        details=DETAILS,
        details_en=DETAILS_EN,
        skills=SKILLS,
        skills_en=SKILLS_EN,
        order=0,
    )


def remove_experience(apps, schema_editor):
    Experience = apps.get_model("core", "Experience")
    Experience.objects.filter(company=COMPANY).delete()
    Experience.objects.update(order=F("order") - 1)


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0018_project_image_help_text"),
    ]

    operations = [
        migrations.RunPython(add_experience, remove_experience),
    ]
