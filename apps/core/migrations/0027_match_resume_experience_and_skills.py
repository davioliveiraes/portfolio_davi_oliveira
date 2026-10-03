# Alinha Experiência Profissional e Competências ao currículo (curriculo.pdf)
# atualizado em 2026-10-02: reagrupa as competências nas 3 trilhas do
# currículo (Backend Python, Engenharia de Dados, IA & Automação) e ajusta
# as atividades/habilidades da Apex Acelera para bater com o texto do PDF.

from django.db import migrations

NEW_CATEGORIES = [
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

# Estado anterior (6 categorias), para reverter.
OLD_CATEGORIES = [
    {
        "name": "Backend & Frameworks",
        "name_en": "Backend & Frameworks",
        "icon": "fas fa-server",
        "order": 0,
        "skills": [
            ("Python", "", "FastAPI, Flask, Django", "", "fab fa-python"),
            ("Django", "", "", "", ""),
            ("FastAPI", "", "", "", ""),
            ("Flask", "", "", "", ""),
            (
                "Go (Golang)",
                "",
                "Em constante evolução",
                "Continuously learning",
                "fab fa-golang",
            ),
            ("APIs RESTful", "RESTful APIs", "", "", "fas fa-file-code"),
            ("Clean Architecture & MVC", "", "", "", "fas fa-cubes"),
            (
                "Integração de serviços externos",
                "External service integration",
                "",
                "",
                "fas fa-plug",
            ),
        ],
    },
    {
        "name": "Inteligência Artificial",
        "name_en": "Artificial Intelligence",
        "icon": "fas fa-brain",
        "order": 2,
        "skills": [
            ("LLMs", "", "", "", "fas fa-robot"),
            ("Pipelines RAG", "RAG Pipelines", "", "", "fas fa-stream"),
            (
                "Modelos Clássicos de ML",
                "Classical ML Models",
                "",
                "",
                "fas fa-microchip",
            ),
            ("Automação de processos", "Process automation", "", "", "fas fa-cogs"),
        ],
    },
    {
        "name": "Dados",
        "name_en": "Data",
        "icon": "fas fa-chart-line",
        "order": 3,
        "skills": [
            ("Pandas", "", "", "", "fas fa-table"),
            ("NumPy", "", "", "", "fas fa-calculator"),
            ("Matplotlib", "", "", "", "fas fa-chart-bar"),
            ("Seaborn", "", "", "", "fas fa-chart-area"),
            ("Excel", "", "", "", "fas fa-file-excel"),
        ],
    },
    {
        "name": "Banco de Dados",
        "name_en": "Databases",
        "icon": "fas fa-database",
        "order": 4,
        "skills": [
            ("PostgreSQL", "", "", "", "fas fa-database"),
            ("MongoDB", "", "", "", "fas fa-database"),
            ("SQLite", "", "", "", "fas fa-database"),
            ("SQLAlchemy & ORM", "", "", "", "fas fa-layer-group"),
        ],
    },
    {
        "name": "DevOps & Infra",
        "name_en": "DevOps & Infra",
        "icon": "fas fa-cloud",
        "order": 5,
        "skills": [
            ("Docker", "", "", "", "fab fa-docker"),
            ("CI/CD (GitHub Actions)", "", "", "", "fas fa-infinity"),
            ("AWS", "", "", "", "fab fa-aws"),
            ("Linux & CLI", "", "", "", "fab fa-linux"),
            ("Nginx + Gunicorn", "", "", "", ""),
        ],
    },
    {
        "name": "Qualidade & Versionamento",
        "name_en": "Quality & Versioning",
        "icon": "fas fa-tools",
        "order": 6,
        "skills": [
            ("Pytest", "", "", "", "fas fa-vial"),
            ("Git", "", "", "", "fab fa-git-alt"),
            ("Pre-commit", "", "", "", ""),
            ("Black & isort", "", "", "", ""),
        ],
    },
]

APEX_ROLE = "Gestor de Dados e Automação com IA"
COMPANY = "Apex Acelera"

NEW_APEX_DETAILS = (
    "Estruturação e gestão de campanhas de tráfego pago, com acompanhamento de "
    "CAC, ROAS e otimização contínua de criativos e segmentação\n"
    "Consolidação de dados dispersos em indicadores de decisão, com "
    "acompanhamento de métricas do funil de vendas\n"
    "Automações e relatórios em Python consumindo APIs externas"
)
NEW_APEX_DETAILS_EN = (
    "Structuring and managing paid traffic campaigns, tracking CAC and ROAS "
    "with continuous optimization of creatives and targeting\n"
    "Consolidating scattered data into decision-making indicators, tracking "
    "sales funnel metrics\n"
    "Automations and reports in Python consuming external APIs"
)
NEW_APEX_SKILLS = (
    "Meta Ads, Tráfego Pago, CAC, ROAS, Dados, Indicadores, Python, APIs, Automação"
)
NEW_APEX_SKILLS_EN = (
    "Meta Ads, Paid Traffic, CAC, ROAS, Data, Indicators, Python, APIs, Automation"
)

OLD_APEX_DETAILS = (
    "Estruturação e gestão de campanhas de tráfego pago, com acompanhamento de "
    "CAC, ROAS e otimização contínua de criativos e segmentação\n"
    "Implantação de CRM e construção de agentes de IA para qualificação e "
    "atendimento automatizado de leads\n"
    "Integração entre plataformas de anúncio, CRM e canais de atendimento, com "
    "automação de funil e relatórios"
)
OLD_APEX_DETAILS_EN = (
    "Structuring and managing paid traffic campaigns, tracking CAC and ROAS "
    "with continuous optimization of creatives and targeting\n"
    "CRM rollout and development of AI agents for automated lead qualification "
    "and support\n"
    "Integration between ad platforms, CRM, and support channels, with funnel "
    "automation and reporting"
)
OLD_APEX_SKILLS = (
    "Meta Ads, CRM, Agentes de IA, Python, APIs, Automação, CAC, ROAS, Funil de Vendas"
)
OLD_APEX_SKILLS_EN = (
    "Meta Ads, CRM, AI Agents, Python, APIs, Automation, CAC, ROAS, Sales Funnel"
)


def _write_categories(apps, categories, skill_width):
    SkillCategory = apps.get_model("core", "SkillCategory")
    Skill = apps.get_model("core", "Skill")
    SkillCategory.objects.all().delete()
    for cat in categories:
        category = SkillCategory.objects.create(
            name=cat["name"],
            name_en=cat["name_en"],
            icon=cat["icon"],
            order=cat["order"],
        )
        for order, skill in enumerate(cat["skills"]):
            if skill_width == 3:
                name, name_en, icon = skill
                detail, detail_en = "", ""
            else:
                name, name_en, detail, detail_en, icon = skill
            Skill.objects.create(
                category=category,
                name=name,
                name_en=name_en,
                detail=detail,
                detail_en=detail_en,
                icon=icon,
                order=order,
            )


def apply_changes(apps, schema_editor):
    _write_categories(apps, NEW_CATEGORIES, skill_width=3)

    Experience = apps.get_model("core", "Experience")
    Experience.objects.filter(company=COMPANY, role=APEX_ROLE).update(
        details=NEW_APEX_DETAILS,
        details_en=NEW_APEX_DETAILS_EN,
        skills=NEW_APEX_SKILLS,
        skills_en=NEW_APEX_SKILLS_EN,
    )


def revert_changes(apps, schema_editor):
    _write_categories(apps, OLD_CATEGORIES, skill_width=5)

    Experience = apps.get_model("core", "Experience")
    Experience.objects.filter(company=COMPANY, role=APEX_ROLE).update(
        details=OLD_APEX_DETAILS,
        details_en=OLD_APEX_DETAILS_EN,
        skills=OLD_APEX_SKILLS,
        skills_en=OLD_APEX_SKILLS_EN,
    )


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0026_add_mongodb_certification"),
    ]

    operations = [
        migrations.RunPython(apply_changes, revert_changes),
    ]
