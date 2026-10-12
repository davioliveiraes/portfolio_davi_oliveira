# Alinha o conteúdo ao currículo (curriculo.pdf) atualizado em 2026-10-12:
# - Competências nas trilhas técnicas do currículo (Python Backend, Python
#   para Dados, Plataformas e SQL, BI e Análise, IA Aplicada e
#   Infraestrutura); a trilha Administrativo fica só no PDF
# - Experiências com as datas completas e as atividades do PDF
# - Os 4 "Projetos selecionados" do currículo no topo, com os textos do PDF
#   (o encurtador de links virou Atalho Prancheta, repositório renomeado,
#   e ganhou preview com a tela da aplicação)

from django.db import migrations

NEW_CATEGORIES = [
    {
        "name": "Python Backend",
        "name_en": "Python Backend",
        "icon": "fas fa-server",
        "order": 0,
        "skills": [
            (
                "FastAPI, Django, DRF e Django Ninja",
                "FastAPI, Django, DRF, and Django Ninja",
                "fab fa-python",
            ),
            ("REST/OpenAPI", "", "fas fa-file-code"),
            ("JWT/OAuth2", "", "fas fa-key"),
            ("ORMs", "", "fas fa-layer-group"),
            ("asyncio", "", "fas fa-bolt"),
            ("Redis/Celery", "", "fas fa-sync-alt"),
            ("Clean Architecture/SOLID", "", "fas fa-cubes"),
            ("Pytest/TDD", "", "fas fa-vial"),
        ],
    },
    {
        "name": "Python para Dados",
        "name_en": "Python for Data",
        "icon": "fas fa-table",
        "order": 1,
        "skills": [
            ("pandas e NumPy", "pandas and NumPy", "fas fa-table"),
            ("scikit-learn", "", "fas fa-microchip"),
            ("ETL/ELT", "", "fas fa-random"),
            ("Apache Airflow", "", "fas fa-wind"),
            (
                "Automação de relatórios via APIs",
                "Report automation via APIs",
                "fas fa-cogs",
            ),
        ],
    },
    {
        "name": "Plataformas e SQL",
        "name_en": "Platforms and SQL",
        "icon": "fas fa-database",
        "order": 2,
        "skills": [
            ("SQL avançado", "Advanced SQL", "fas fa-database"),
            ("PostgreSQL (PL/pgSQL, triggers)", "", "fas fa-database"),
            ("MongoDB", "", "fas fa-database"),
            ("Databricks", "", "fas fa-cloud"),
            (
                "Modelagem relacional/dimensional",
                "Relational/dimensional modeling",
                "fas fa-project-diagram",
            ),
            ("Data warehouse", "", "fas fa-warehouse"),
            ("Qualidade de dados", "Data quality", "fas fa-check-double"),
        ],
    },
    {
        "name": "BI e Análise",
        "name_en": "BI and Analytics",
        "icon": "fas fa-chart-line",
        "order": 3,
        "skills": [
            ("Excel", "", "fas fa-file-excel"),
            ("Power BI", "", "fas fa-chart-pie"),
            (
                "Dashboards e relatórios gerenciais",
                "Dashboards and management reports",
                "fas fa-chart-bar",
            ),
            (
                "KPIs, CAC, ROAS e funil de vendas",
                "KPIs, CAC, ROAS, and sales funnel",
                "fas fa-chart-line",
            ),
        ],
    },
    {
        "name": "IA Aplicada",
        "name_en": "Applied AI",
        "icon": "fas fa-brain",
        "order": 4,
        "skills": [
            ("LLMs via API (Claude, OpenAI, Gemini)", "", "fas fa-robot"),
            ("RAG/pgvector", "", "fas fa-stream"),
            ("Agentes de IA", "AI agents", "fas fa-microchip"),
            ("Extração de documentos", "Document extraction", "fas fa-file-alt"),
        ],
    },
    {
        "name": "Infraestrutura",
        "name_en": "Infrastructure",
        "icon": "fas fa-cloud",
        "order": 5,
        "skills": [
            ("Docker/Compose", "", "fab fa-docker"),
            ("Linux", "", "fab fa-linux"),
            ("Nginx e Gunicorn", "Nginx and Gunicorn", "fas fa-server"),
            ("GitHub Actions", "", "fas fa-infinity"),
            ("Git/GitFlow", "", "fab fa-git-alt"),
            ("Deploy em VPS", "VPS deployment", "fas fa-cloud-upload-alt"),
        ],
    },
]

# Estado deixado pela 0027 (3 trilhas), para reverter.
OLD_CATEGORIES = [
    {
        "name": "Backend Python",
        "name_en": "Backend Python",
        "icon": "fas fa-server",
        "order": 0,
        "skills": [
            ("Python (FastAPI, Django, DRF, Django Ninja)", "", "fab fa-python"),
            ("REST/OpenAPI", "", "fas fa-file-code"),
            ("JWT/OAuth2", "", "fas fa-key"),
            ("ORMs e migrações", "ORMs and migrations", "fas fa-layer-group"),
            ("asyncio", "", "fas fa-bolt"),
            ("Redis/Celery", "", "fas fa-sync-alt"),
            ("Clean Architecture/SOLID", "", "fas fa-cubes"),
            ("Pytest/TDD", "", "fas fa-vial"),
        ],
    },
    {
        "name": "Engenharia de Dados",
        "name_en": "Data Engineering",
        "icon": "fas fa-database",
        "order": 1,
        "skills": [
            ("SQL avançado", "Advanced SQL", "fas fa-database"),
            (
                "PostgreSQL, MongoDB e SQLite",
                "PostgreSQL, MongoDB, and SQLite",
                "fas fa-database",
            ),
            (
                "Modelagem relacional/dimensional",
                "Relational/dimensional modeling",
                "fas fa-project-diagram",
            ),
            ("ETL/ELT", "", "fas fa-random"),
            ("pandas/NumPy", "", "fas fa-table"),
            ("Qualidade de dados", "Data quality", "fas fa-check-double"),
            (
                "KPIs, CAC, ROAS e funil",
                "KPIs, CAC, ROAS, and funnel",
                "fas fa-chart-line",
            ),
            ("Dashboards", "", "fas fa-chart-bar"),
        ],
    },
    {
        "name": "IA & Automação",
        "name_en": "AI & Automation",
        "icon": "fas fa-brain",
        "order": 2,
        "skills": [
            (
                "LLMs via API e open source (Claude, OpenAI, Gemini, Hugging "
                "Face/Ollama)",
                "LLMs via API and open source (Claude, OpenAI, Gemini, Hugging "
                "Face/Ollama)",
                "fas fa-robot",
            ),
            ("Structured outputs", "", "fas fa-file-code"),
            ("Function calling", "", "fas fa-code"),
            ("RAG/pgvector", "", "fas fa-stream"),
            ("Agentes de IA", "AI agents", "fas fa-microchip"),
            ("MCP", "", "fas fa-plug"),
            (
                "APIs, webhooks e workflows",
                "APIs, webhooks, and workflows",
                "fas fa-cogs",
            ),
        ],
    },
]

# Experiências: empresa -> (campos antes, campos depois)
EXPERIENCES = {
    "Apex Acelera": (
        {
            "period_en": "Aug 2026 to today · Remote",
            "details": (
                "Estruturação e gestão de campanhas de tráfego pago, com "
                "acompanhamento de CAC, ROAS e otimização contínua de criativos "
                "e segmentação\n"
                "Consolidação de dados dispersos em indicadores de decisão, com "
                "acompanhamento de métricas do funil de vendas\n"
                "Automações e relatórios em Python consumindo APIs externas"
            ),
            "details_en": (
                "Structuring and managing paid traffic campaigns, tracking CAC "
                "and ROAS with continuous optimization of creatives and "
                "targeting\n"
                "Consolidating scattered data into decision-making indicators, "
                "tracking sales funnel metrics\n"
                "Automations and reports in Python consuming external APIs"
            ),
        },
        {
            "period_en": "Aug 2026 to present · Remote",
            "details": (
                "Estruturação e gestão de campanhas de tráfego pago, com "
                "acompanhamento de CAC, ROAS e otimização contínua de criativos\n"
                "Consolidação de dados dispersos em indicadores de decisão, com "
                "acompanhamento de métricas do funil de vendas\n"
                "Automações e relatórios em Python consumindo APIs externas"
            ),
            "details_en": (
                "Structuring and managing paid traffic campaigns, tracking CAC "
                "and ROAS with continuous optimization of creatives\n"
                "Consolidating scattered data into decision-making indicators, "
                "tracking sales funnel metrics\n"
                "Automations and reports in Python consuming external APIs"
            ),
        },
    ),
    "Hiper Morada Nova": (
        {
            "period": "2021 a 2025 · Morada Nova, CE",
            "period_en": "2021 to 2025 · Morada Nova, CE",
            "details": (
                "Gerenciei o ciclo completo de entrada e saída de NF-e via "
                "SysPDV, garantindo correta emissão, conferência tributária e "
                "conformidade fiscal diária.\n"
                "Desenvolvi e implementei dashboards automatizados em Excel, "
                "transformando dados brutos em insights de negócio.\n"
                "Automatizei análises e relatórios administrativos, melhorando "
                "a precisão e eficiência operacional.\n"
                "Prestei suporte técnico a sistemas e equipamentos, garantindo "
                "a continuidade operacional do SysPDV."
            ),
            "details_en": (
                "Managed the complete inbound and outbound NF-e cycle through "
                "SysPDV, ensuring correct issuance, tax verification, and daily "
                "fiscal compliance.\n"
                "Developed and implemented automated Excel dashboards, turning "
                "raw data into business insights.\n"
                "Automated administrative analyses and reports, improving "
                "accuracy and operational efficiency.\n"
                "Provided technical support for systems and equipment, ensuring "
                "the operational continuity of SysPDV."
            ),
            "skills": "Excel, Dashboards, Automação de Relatórios, SysPDV, Suporte Técnico",
            "skills_en": "Excel, Dashboards, Report Automation, SysPDV, Technical Support",
        },
        {
            "period": "Abr 2021 a Abr 2025 · Morada Nova, CE",
            "period_en": "Apr 2021 to Apr 2025 · Morada Nova, CE",
            "details": (
                "Gerenciei o ciclo de NF-e via SysPDV, com conferência "
                "tributária e conformidade fiscal diária\n"
                "Desenvolvi dashboards e relatórios automatizados em Excel, "
                "transformando dados brutos em insights de negócio\n"
                "Como Jovem Aprendiz, organizei boletos e processos "
                "administrativos e ofereci suporte técnico básico"
            ),
            "details_en": (
                "Managed the NF-e cycle through SysPDV, with tax verification "
                "and daily fiscal compliance\n"
                "Developed automated Excel dashboards and reports, turning raw "
                "data into business insights\n"
                "As a Young Apprentice, organized payment slips and "
                "administrative processes and provided basic technical support"
            ),
            "skills": (
                "NF-e, SysPDV, Excel, Dashboards, Automação de Relatórios, "
                "Suporte Técnico"
            ),
            "skills_en": (
                "NF-e, SysPDV, Excel, Dashboards, Report Automation, "
                "Technical Support"
            ),
        },
    ),
    "Betânia Lácteos": (
        {
            "period": "2020 a 2021 · Morada Nova, CE",
            "period_en": "2020 to 2021 · Morada Nova, CE",
            "details": (
                "Organizei documentação fiscal e planilhas administrativas, "
                "aprimorando o controle de dados.\n"
                "Desenvolvi atenção a detalhes e precisão em registros "
                "administrativos."
            ),
            "details_en": (
                "Organized fiscal documentation and administrative "
                "spreadsheets, improving data control.\n"
                "Developed attention to detail and accuracy in administrative "
                "records."
            ),
        },
        {
            "period": "Fev 2020 a Mar 2021 · Morada Nova, CE",
            "period_en": "Feb 2020 to Mar 2021 · Morada Nova, CE",
            "details": (
                "Organizei documentação fiscal e planilhas administrativas, "
                "aprimorando o controle de dados"
            ),
            "details_en": (
                "Organized fiscal documentation and administrative "
                "spreadsheets, improving data control"
            ),
        },
    ),
    "Prisma Informática": (
        {
            "role": "Estagiário",
            "role_en": "Intern",
            "period": "2017 · Morada Nova, CE",
            "period_en": "2017 · Morada Nova, CE",
            "details": (
                "Iniciei contato com desenvolvimento web (HTML5, CSS3 e "
                "JavaScript), compreendendo a integração front-end e back-end.\n"
                "Ofereci suporte técnico e atendimento a clientes, fortalecendo "
                "comunicação e resolução de problemas."
            ),
            "details_en": (
                "Started working with web development (HTML5, CSS3, and "
                "JavaScript), understanding front-end and back-end "
                "integration.\n"
                "Provided technical support and customer service, strengthening "
                "communication and problem-solving skills."
            ),
            "skills": "Lógica de Programação, Suporte Técnico, Atendimento ao Cliente",
            "skills_en": "Programming Logic, Technical Support, Customer Service",
        },
        {
            "role": "Estagiário de TI",
            "role_en": "IT Intern",
            "period": "Ago 2017 a Dez 2017 · Morada Nova, CE",
            "period_en": "Aug 2017 to Dec 2017 · Morada Nova, CE",
            "details": (
                "Ofereci suporte técnico e atendimento a clientes e tive o "
                "primeiro contato com desenvolvimento web"
            ),
            "details_en": (
                "Provided technical support and customer service, and had my "
                "first contact with web development"
            ),
            "skills": "Suporte Técnico, Atendimento ao Cliente, Desenvolvimento Web",
            "skills_en": "Technical Support, Customer Service, Web Development",
        },
    ),
}

# Projetos: (campo que identifica o projeto, campos antes, campos depois).
# "order" (Destaque) põe os 4 projetos do currículo no topo, na mesma ordem.
PROJECTS = [
    (
        "github_url",
        {
            "github_url": "https://github.com/davioliveiraes/apex-reports",
            "description": (
                "Relatórios em PDF com dados do Meta Ads, quatro modos de "
                "análise e KPIs automáticos."
            ),
            "description_en": (
                "PDF reports from Meta Ads data, with four analysis modes and "
                "automated KPIs."
            ),
            "order": 0,
        },
        {
            "github_url": "https://github.com/davioliveiraes/apex-reports",
            "description": (
                "Gerador de relatórios PDF a partir do Meta Ads, com KPIs "
                "automatizados e deploy em VPS."
            ),
            "description_en": (
                "PDF report generator from Meta Ads data, with automated KPIs "
                "and VPS deployment."
            ),
            "order": 4,
        },
    ),
    (
        "github_url",
        {
            "github_url": "https://github.com/davioliveiraes/ecommerce-control",
            "description": (
                "Painel multi-tenant que integra Nuvemshop e GestãoClick para "
                "centralizar a operação."
            ),
            "description_en": (
                "Multi-tenant dashboard integrating Nuvemshop and GestãoClick "
                "into one operation."
            ),
            "tags": "Django Ninja, PostgreSQL, Docker, JWT",
            "order": 0,
        },
        {
            "github_url": "https://github.com/davioliveiraes/ecommerce-control",
            "description": (
                "Painel multi-tenant para lojistas NuvemShop e GestãoClick."
            ),
            "description_en": (
                "Multi-tenant dashboard for NuvemShop and GestãoClick merchants."
            ),
            "tags": "Django Ninja, PostgreSQL, React, Docker",
            "order": 3,
        },
    ),
    (
        "github_url",
        {
            "github_url": "https://github.com/davioliveiraes/url_shortener_api",
            "title": "API Encurtador de Links",
            "title_en": "URL Shortener API",
            "description": (
                "Encurtador de URLs com rastreamento de cliques, geração de QR "
                "Codes e painel administrativo de métricas."
            ),
            "description_en": (
                "URL shortener with click tracking, QR Code generation, and an "
                "administrative metrics dashboard."
            ),
            "tags": "Django REST Framework, PostgreSQL, Docker",
            "image": "",
            "order": 0,
        },
        {
            "github_url": "https://github.com/davioliveiraes/atalho-prancheta",
            "title": "Atalho Prancheta",
            "title_en": "Atalho Prancheta",
            "description": (
                "Encurtador de links com destino editável, QR Code, métricas de "
                "cliques e 272 testes."
            ),
            "description_en": (
                "Link shortener with editable destinations, QR Codes, click "
                "metrics, and 272 tests."
            ),
            "tags": "Django, DRF, PostgreSQL, Redis",
            "image": "images/projects/atalho-prancheta.webp",
            "order": 2,
        },
    ),
    (
        "live_url",
        {
            "live_url": "https://ibeize.com.br",
            "title": "E-commerce Ibeize",
            "title_en": "Ibeize E-commerce",
            "description": (
                "E-commerce integrado ao GestãoClick, com GoTemplate, Melhor "
                "Envio e estoque sincronizado."
            ),
            "description_en": (
                "E-commerce integrated with GestãoClick, GoTemplate, Melhor "
                "Envio, and synchronized inventory."
            ),
            "tags": "NuvemShop, GoTemplate, GestãoClick, Integração de API",
            "order": 0,
        },
        {
            "live_url": "https://ibeize.com.br",
            "title": "E-commerce iBeize",
            "title_en": "iBeize E-commerce",
            "description": (
                "Storefront customizado com integração contínua de catálogo e "
                "pedidos ao ERP."
            ),
            "description_en": (
                "Custom storefront with continuous catalog and order "
                "integration with the ERP."
            ),
            "tags": "NuvemShop, GoTemplate, GestãoClick",
            "order": 1,
        },
    ),
]


def _write_categories(apps, alias, categories):
    SkillCategory = apps.get_model("core", "SkillCategory")
    Skill = apps.get_model("core", "Skill")
    SkillCategory.objects.using(alias).all().delete()
    for cat in categories:
        category = SkillCategory.objects.using(alias).create(
            name=cat["name"],
            name_en=cat["name_en"],
            icon=cat["icon"],
            order=cat["order"],
        )
        for order, (name, name_en, icon) in enumerate(cat["skills"]):
            Skill.objects.using(alias).create(
                category=category,
                name=name,
                name_en=name_en,
                icon=icon,
                order=order,
            )


def _write_content(apps, alias, forward):
    # Índices nas tuplas (antes, depois) de EXPERIENCES e PROJECTS
    before, after = (0, 1) if forward else (1, 0)
    _write_categories(apps, alias, NEW_CATEGORIES if forward else OLD_CATEGORIES)

    Experience = apps.get_model("core", "Experience")
    for company, states in EXPERIENCES.items():
        Experience.objects.using(alias).filter(company=company).update(**states[after])

    Project = apps.get_model("core", "Project")
    for key, *states in PROJECTS:
        # O projeto é localizado pelo valor que tem agora (a URL do encurtador
        # muda junto com o nome do repositório)
        Project.objects.using(alias).filter(**{key: states[before][key]}).update(
            **states[after]
        )


def apply_content(apps, schema_editor):
    _write_content(apps, schema_editor.connection.alias, forward=True)


def restore_content(apps, schema_editor):
    _write_content(apps, schema_editor.connection.alias, forward=False)


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0028_contact_ordering_tiebreak"),
    ]

    operations = [
        migrations.RunPython(apply_content, restore_content),
    ]
