# Atualiza as atividades informadas e a captura do projeto Apex.
# Mantém cargos, períodos, habilidades, ordem e descrições dos projetos.
from django.db import migrations

PROJECT_TITLE = "Apex Acelera | Reports"
NEW_IMAGE = "images/projects/apex-reports-overview.png"
OLD_IMAGE = "images/projects/apex-reports.png"

NEW_DETAILS = {
    "Apex Acelera": (
        (
            "Estruturação e gestão de campanhas de tráfego pago, com "
            "acompanhamento de CAC, ROAS e otimização contínua de criativos e "
            "segmentação\n"
            "Implantação de CRM e construção de agentes de IA para qualificação e "
            "atendimento automatizado de leads\n"
            "Integração entre plataformas de anúncio, CRM e canais de "
            "atendimento, com automação de funil e relatórios"
        ),
        (
            "Structuring and managing paid traffic campaigns, tracking CAC and "
            "ROAS with continuous optimization of creatives and targeting\n"
            "CRM rollout and development of AI agents for automated lead "
            "qualification and support\n"
            "Integration between ad platforms, CRM, and support channels, with "
            "funnel automation and reporting"
        ),
    ),
    "iBeize": (
        (
            "Análise de resultados, experimentação e otimizações contínuas da "
            "loja NuvemShop\n"
            "Customização do storefront via CSS/HTML/JS/GoTemplate avançado e "
            "integração com ERP GestãoClick\n"
            "Configuração de DNS, integração com Melhor Envio e alinhamento de "
            "SKUs com estoque\n"
            "Suporte em ações comerciais e integração com operação logística"
        ),
        (
            "Results analysis, experimentation, and continuous optimizations for "
            "the NuvemShop store\n"
            "Storefront customization via advanced CSS/HTML/JS/GoTemplate and "
            "integration with GestãoClick ERP\n"
            "DNS configuration, integration with Melhor Envio, and SKU alignment "
            "with inventory\n"
            "Support for commercial actions and integration with logistics "
            "operations"
        ),
    ),
    "Hiper Morada Nova": (
        (
            "Gerenciei o ciclo completo de entrada e saída de NF-e via SysPDV, "
            "garantindo correta emissão, conferência tributária e conformidade "
            "fiscal diária.\n"
            "Desenvolvi e implementei dashboards automatizados em Excel, "
            "transformando dados brutos em insights de negócio.\n"
            "Automatizei análises e relatórios administrativos, melhorando a "
            "precisão e eficiência operacional.\n"
            "Prestei suporte técnico a sistemas e equipamentos, garantindo a "
            "continuidade operacional do SysPDV."
        ),
        (
            "Managed the complete inbound and outbound NF-e cycle through SysPDV, "
            "ensuring correct issuance, tax verification, and daily fiscal "
            "compliance.\n"
            "Developed and implemented automated Excel dashboards, turning raw "
            "data into business insights.\n"
            "Automated administrative analyses and reports, improving accuracy "
            "and operational efficiency.\n"
            "Provided technical support for systems and equipment, ensuring the "
            "operational continuity of SysPDV."
        ),
    ),
    "Betânia Lácteos": (
        (
            "Organizei documentação fiscal e planilhas administrativas, "
            "aprimorando o controle de dados.\n"
            "Desenvolvi atenção a detalhes e precisão em registros "
            "administrativos."
        ),
        (
            "Organized fiscal documentation and administrative spreadsheets, "
            "improving data control.\n"
            "Developed attention to detail and accuracy in administrative "
            "records."
        ),
    ),
    "Prisma Informática": (
        (
            "Iniciei contato com desenvolvimento web (HTML5, CSS3 e JavaScript), "
            "compreendendo a integração front-end e back-end.\n"
            "Ofereci suporte técnico e atendimento a clientes, fortalecendo "
            "comunicação e resolução de problemas."
        ),
        (
            "Started working with web development (HTML5, CSS3, and JavaScript), "
            "understanding front-end and back-end integration.\n"
            "Provided technical support and customer service, strengthening "
            "communication and problem-solving skills."
        ),
    ),
}

OLD_DETAILS = {
    "Apex Acelera": (
        (
            "Estruturação e gestão de campanhas de tráfego pago, com "
            "acompanhamento de CAC, ROAS e otimização contínua de criativos e "
            "segmentação\n"
            "Implantação de CRM e construção de agentes de IA para qualificação e "
            "atendimento automatizado de leads\n"
            "Integração entre plataformas de anúncio, CRM e canais de "
            "atendimento, com automação de funil e relatórios"
        ),
        (
            "Structuring and managing paid traffic campaigns, tracking CAC and "
            "ROAS with continuous optimization of creatives and targeting\n"
            "CRM rollout and development of AI agents for automated lead "
            "qualification and support\n"
            "Integration between ad platforms, CRM, and support channels, with "
            "funnel automation and reporting"
        ),
    ),
    "iBeize": (
        (
            "Análise de resultados, experimentação e otimizações contínuas da "
            "loja NuvemShop\n"
            "Integração com o ERP GestãoClick e customização do storefront via "
            "GoTemplate\n"
            "Configuração de DNS, integração com Melhor Envio e alinhamento de "
            "SKUs com o estoque, apoiando ações comerciais e a operação logística"
        ),
        (
            "Results analysis, experimentation, and continuous optimizations for "
            "the NuvemShop store\n"
            "Integration with the GestãoClick ERP and storefront customization "
            "via GoTemplate\n"
            "DNS configuration, Melhor Envio integration, and SKU alignment with "
            "inventory, supporting commercial actions and logistics operations"
        ),
    ),
    "Hiper Morada Nova": (
        (
            "Desenvolvi dashboards automatizados em Excel, transformando dados "
            "brutos em insights de negócio\n"
            "Automatizei relatórios administrativos com lógica de processamento "
            "que reduziu o tempo de geração em até 60%\n"
            "Prestei suporte técnico a sistemas e equipamentos, garantindo a "
            "continuidade operacional do SysPDV"
        ),
        (
            "Built automated Excel dashboards, turning raw data into business "
            "insights\n"
            "Automated administrative reports with processing logic that cut "
            "generation time by up to 60%\n"
            "Provided technical support for systems and equipment, ensuring "
            "operational continuity of SysPDV"
        ),
    ),
    "Betânia Lácteos": (
        (
            "Organizei documentação fiscal e planilhas administrativas, "
            "aprimorando o controle de dados\n"
            "Apoiei as rotinas administrativas do setor, com conferência de "
            "registros e arquivamento de documentos\n"
            "Desenvolvi atenção a detalhes e precisão em registros "
            "administrativos"
        ),
        (
            "Organized fiscal documentation and administrative spreadsheets, "
            "improving data control\n"
            "Supported the department's administrative routines, checking records "
            "and filing documents\n"
            "Developed attention to detail and accuracy in administrative records"
        ),
    ),
    "Prisma Informática": (
        (
            "Iniciei contato com programação e lógica de desenvolvimento de "
            "sistemas\n"
            "Ofereci suporte técnico e atendimento a clientes, fortalecendo "
            "comunicação e resolução de problemas\n"
            "Auxiliei na manutenção e configuração de computadores e periféricos, "
            "acompanhando os chamados até a resolução"
        ),
        (
            "Started working with programming and systems development logic\n"
            "Provided technical support and customer service, strengthening "
            "communication and problem-solving skills\n"
            "Assisted with the maintenance and setup of computers and "
            "peripherals, following tickets through to resolution"
        ),
    ),
}


def apply_content(apps, schema_editor):
    alias = schema_editor.connection.alias
    Experience = apps.get_model("core", "Experience")
    Project = apps.get_model("core", "Project")
    for company, (details, details_en) in NEW_DETAILS.items():
        Experience.objects.using(alias).filter(company=company).update(
            details=details, details_en=details_en
        )
    Project.objects.using(alias).filter(title=PROJECT_TITLE).update(image=NEW_IMAGE)


def restore_content(apps, schema_editor):
    alias = schema_editor.connection.alias
    Experience = apps.get_model("core", "Experience")
    Project = apps.get_model("core", "Project")
    for company, (details, details_en) in OLD_DETAILS.items():
        current, current_en = NEW_DETAILS[company]
        Experience.objects.using(alias).filter(
            company=company, details=current, details_en=current_en
        ).update(details=details, details_en=details_en)
    Project.objects.using(alias).filter(title=PROJECT_TITLE, image=NEW_IMAGE).update(
        image=OLD_IMAGE
    )


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0024_shorten_image_project_previews"),
    ]

    operations = [
        migrations.RunPython(apply_content, restore_content),
    ]
