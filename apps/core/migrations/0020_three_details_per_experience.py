# Padroniza as experiências em exatamente três tópicos cada: as que tinham
# quatro foram resumidas e as que tinham duas ganharam um terceiro relacionado.

from django.db import migrations

NEW_DETAILS = {
    "Apex Acelera": (
        (
            "Estruturação e gestão de campanhas de tráfego pago, com "
            "acompanhamento de CAC, ROAS e otimização contínua de criativos e "
            "segmentação\n"
            "Implantação de CRM e construção de agentes de IA para qualificação "
            "e atendimento automatizado de leads\n"
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
            "integração com o ERP GestãoClick\n"
            "Configuração de DNS, integração com Melhor Envio e alinhamento de "
            "SKUs com o estoque, apoiando ações comerciais e a operação "
            "logística"
        ),
        (
            "Results analysis, experimentation, and continuous optimizations "
            "for the NuvemShop store\n"
            "Storefront customization via advanced CSS/HTML/JS/GoTemplate and "
            "integration with the GestãoClick ERP\n"
            "DNS configuration, Melhor Envio integration, and SKU alignment "
            "with inventory, supporting commercial actions and logistics "
            "operations"
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
            "Supported the department's administrative routines, checking "
            "records and filing documents\n"
            "Developed attention to detail and accuracy in administrative "
            "records"
        ),
    ),
    "Prisma Informática": (
        (
            "Iniciei contato com desenvolvimento web (HTML5, CSS3 e "
            "JavaScript)\n"
            "Ofereci suporte técnico e atendimento a clientes, fortalecendo "
            "comunicação e resolução de problemas\n"
            "Auxiliei na manutenção e configuração de computadores e "
            "periféricos, acompanhando os chamados até a resolução"
        ),
        (
            "Started working with web development (HTML5, CSS3, and "
            "JavaScript)\n"
            "Provided technical support and customer service, strengthening "
            "communication and problem-solving skills\n"
            "Assisted with the maintenance and setup of computers and "
            "peripherals, following tickets through to resolution"
        ),
    ),
}

OLD_DETAILS = {
    "Apex Acelera": (
        (
            "Responsável pelos dois principais serviços da agência: "
            "Tráfego Pago e CRM com Agente de IA\n"
            "Estruturação e gestão de campanhas de tráfego pago, com "
            "acompanhamento de CAC, ROAS e otimização contínua de criativos e "
            "segmentação\n"
            "Implantação de CRM e construção de agentes de IA para qualificação "
            "e atendimento automatizado de leads\n"
            "Integração entre plataformas de anúncio, CRM e canais de "
            "atendimento, com automação de funil e relatórios"
        ),
        (
            "Responsible for the agency's two main services: "
            "Paid Traffic and CRM with an AI Agent\n"
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
            "Results analysis, experimentation, and continuous optimizations "
            "for the NuvemShop store\n"
            "Storefront customization via advanced CSS/HTML/JS/GoTemplate and "
            "integration with GestãoClick ERP\n"
            "DNS configuration, integration with Melhor Envio, and SKU "
            "alignment with inventory\n"
            "Support for commercial actions and integration with logistics "
            "operations"
        ),
    ),
    "Hiper Morada Nova": (
        (
            "Desenvolvi dashboards automatizados em Excel, transformando dados "
            "brutos em insights de negócio\n"
            "Otimizei relatórios internos com lógica de processamento que "
            "reduziu o tempo de geração em até 60%\n"
            "Automatizei análises e relatórios administrativos, melhorando a "
            "precisão e eficiência operacional\n"
            "Prestei suporte técnico a sistemas e equipamentos, garantindo a "
            "continuidade operacional do SysPDV"
        ),
        (
            "Built automated Excel dashboards, turning raw data into business "
            "insights\n"
            "Optimized internal reports with processing logic that reduced "
            "generation time by up to 60%\n"
            "Automated administrative analyses and reports, improving accuracy "
            "and operational efficiency\n"
            "Provided technical support for systems and equipment, ensuring "
            "operational continuity of SysPDV"
        ),
    ),
    "Betânia Lácteos": (
        (
            "Organizei documentação fiscal e planilhas administrativas, "
            "aprimorando o controle de dados\n"
            "Desenvolvi atenção a detalhes e precisão em registros "
            "administrativos"
        ),
        (
            "Organized fiscal documentation and administrative spreadsheets, "
            "improving data control\n"
            "Developed attention to detail and accuracy in administrative "
            "records"
        ),
    ),
    "Prisma Informática": (
        (
            "Iniciei contato com desenvolvimento web (HTML5, CSS3 e "
            "JavaScript)\n"
            "Ofereci suporte técnico e atendimento a clientes, fortalecendo "
            "comunicação e resolução de problemas"
        ),
        (
            "Started working with web development (HTML5, CSS3, and "
            "JavaScript)\n"
            "Provided technical support and customer service, strengthening "
            "communication and problem-solving skills"
        ),
    ),
}


def apply_details(apps, mapping):
    Experience = apps.get_model("core", "Experience")
    for company, (details, details_en) in mapping.items():
        Experience.objects.filter(company=company).update(
            details=details,
            details_en=details_en,
        )


def trim_details(apps, schema_editor):
    apply_details(apps, NEW_DETAILS)


def restore_details(apps, schema_editor):
    apply_details(apps, OLD_DETAILS)


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0019_add_apex_acelera_experience"),
    ]

    operations = [
        migrations.RunPython(trim_details, restore_details),
    ]
