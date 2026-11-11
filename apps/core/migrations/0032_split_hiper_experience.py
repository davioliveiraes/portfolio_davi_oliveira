# Separa a Hiper Morada Nova em duas experiências, como no currículo
# (curriculo.pdf atualizado em 2026-11-11):
# - Assistente Administrativo, abr 2022 a abr 2025
# - Jovem Aprendiz, abr 2021 a abr 2022 (antes era uma linha "Como Jovem
#   Aprendiz, ..." dentro da experiência de Assistente Administrativo)
# Betânia Lácteos e Prisma Informática descem uma posição.

from django.db import migrations

COMPANY = "Hiper Morada Nova"
ASSISTANT_ROLE = "Assistente Administrativo"

# Assistente Administrativo: (campos antes, campos depois)
ASSISTANT = (
    {
        "period": "Abr 2021 a Abr 2025 · Morada Nova, CE",
        "period_en": "Apr 2021 to Apr 2025 · Morada Nova, CE",
        "details": (
            "Gerenciei o ciclo de NF-e via SysPDV, com conferência tributária e "
            "conformidade fiscal diária\n"
            "Desenvolvi dashboards e relatórios automatizados em Excel, "
            "transformando dados brutos em insights de negócio\n"
            "Como Jovem Aprendiz, organizei boletos e processos administrativos "
            "e ofereci suporte técnico básico"
        ),
        "details_en": (
            "Managed the NF-e cycle through SysPDV, with tax verification and "
            "daily fiscal compliance\n"
            "Developed automated Excel dashboards and reports, turning raw data "
            "into business insights\n"
            "As a Young Apprentice, organized payment slips and administrative "
            "processes and provided basic technical support"
        ),
        "skills": (
            "NF-e, SysPDV, Excel, Dashboards, Automação de Relatórios, "
            "Suporte Técnico"
        ),
        "skills_en": (
            "NF-e, SysPDV, Excel, Dashboards, Report Automation, Technical Support"
        ),
    },
    {
        "period": "Abr 2022 a Abr 2025 · Morada Nova, CE",
        "period_en": "Apr 2022 to Apr 2025 · Morada Nova, CE",
        "details": (
            "Gerenciei o ciclo de NF-e via SysPDV, com conferência tributária e "
            "conformidade fiscal diária\n"
            "Desenvolvi dashboards e relatórios automatizados em Excel, "
            "transformando dados brutos em insights de negócio"
        ),
        "details_en": (
            "Managed the NF-e cycle through SysPDV, with tax verification and "
            "daily fiscal compliance\n"
            "Developed automated Excel dashboards and reports, turning raw data "
            "into business insights"
        ),
        "skills": "NF-e, SysPDV, Excel, Dashboards, Automação de Relatórios",
        "skills_en": "NF-e, SysPDV, Excel, Dashboards, Report Automation",
    },
)

APPRENTICE = {
    "company": COMPANY,
    "role": "Jovem Aprendiz",
    "role_en": "Young Apprentice",
    "period": "Abr 2021 a Abr 2022 · Morada Nova, CE",
    "period_en": "Apr 2021 to Apr 2022 · Morada Nova, CE",
    "details": (
        "Organizei boletos e processos administrativos e ofereci suporte "
        "técnico básico"
    ),
    "details_en": (
        "Organized payment slips and administrative processes and provided "
        "basic technical support"
    ),
    "skills": "Boletos, Processos Administrativos, Suporte Técnico",
    "skills_en": "Payment Slips, Administrative Processes, Technical Support",
    "order": 3,
}

# Experiências que mudam de posição: empresa -> (ordem antes, ordem depois)
ORDERS = {
    "Betânia Lácteos": (3, 4),
    "Prisma Informática": (4, 5),
}


def apply_content(apps, schema_editor):
    alias = schema_editor.connection.alias
    Experience = apps.get_model("core", "Experience")
    for company, (_before, after) in ORDERS.items():
        Experience.objects.using(alias).filter(company=company).update(order=after)
    Experience.objects.using(alias).filter(company=COMPANY, role=ASSISTANT_ROLE).update(
        **ASSISTANT[1]
    )
    Experience.objects.using(alias).get_or_create(
        company=COMPANY, role=APPRENTICE["role"], defaults=APPRENTICE
    )


def restore_content(apps, schema_editor):
    alias = schema_editor.connection.alias
    Experience = apps.get_model("core", "Experience")
    Experience.objects.using(alias).filter(
        company=COMPANY, role=APPRENTICE["role"]
    ).delete()
    Experience.objects.using(alias).filter(company=COMPANY, role=ASSISTANT_ROLE).update(
        **ASSISTANT[0]
    )
    for company, (before, _after) in ORDERS.items():
        Experience.objects.using(alias).filter(company=company).update(order=before)


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0031_remove_ecommerce_control"),
    ]

    operations = [
        migrations.RunPython(apply_content, restore_content),
    ]
