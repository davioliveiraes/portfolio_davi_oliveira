# Cura dos projetos (2026-10-12):
# - Remove as 6 APIs Flask de estudo; elas continuam no GitHub
# - As coleções python-projects e data_science_projects ganham capas geradas
#   por scripts/collection_previews.py e vão para o final da lista
# - Apex Reports: sem botão "Código" (repositório privado) e preview em webp
# - Ecommerce Control passa para Projetos Técnicos
# - Ordem explícita pelo Destaque: currículo, portfólio e, por fim, coleções

from django.db import migrations

GITHUB = "https://github.com/davioliveiraes/"

REMOVED_PROJECTS = [
    {
        "title": "API de Pedidos com JWT",
        "title_en": "JWT Order API",
        "description": (
            "API de pedidos com autenticação JWT, isolamento de dados por usuário, "
            "arquitetura em camadas e testes automatizados."
        ),
        "description_en": (
            "Order API with JWT authentication, per-user data isolation, layered "
            "architecture, and automated tests."
        ),
        "tags": "Flask, PyJWT, bcrypt, SQLite, Pytest",
        "tags_en": "",
        "github_url": GITHUB + "jwt_order_api",
    },
    {
        "title": "API Bancária Segura com JWT",
        "title_en": "JWT Secured Banking API",
        "description": (
            "API bancária com autenticação JWT, senhas protegidas por bcrypt, "
            "arquitetura em camadas e testes automatizados."
        ),
        "description_en": (
            "Banking API with JWT authentication, bcrypt password protection, "
            "layered architecture, and automated tests."
        ),
        "tags": "Flask, PyJWT, bcrypt, SQLite, Pytest",
        "tags_en": "",
        "github_url": GITHUB + "jwt_secured_banking_api",
    },
    {
        "title": "Chat em Tempo Real",
        "title_en": "Real-Time Chat",
        "description": (
            "Sistema de mensagens bidirecionais em tempo real desenvolvido com "
            "WebSockets."
        ),
        "description_en": (
            "Real-time bidirectional messaging system built with WebSockets."
        ),
        "tags": "Flask-SocketIO, WebSockets",
        "tags_en": "",
        "github_url": GITHUB + "flask_realtime_chat_socket",
    },
    {
        "title": "API de Adoção de Pets",
        "title_en": "Pet Adoption API",
        "description": (
            "API para gestão de adoções de pets, estruturada com Clean "
            "Architecture, MVC e separação entre casos de uso e repositórios."
        ),
        "description_en": (
            "Pet adoption management API structured with Clean Architecture, MVC, "
            "and separated use cases and repositories."
        ),
        "tags": "Flask, Clean Architecture, MVC, Pytest",
        "tags_en": "",
        "github_url": GITHUB + "pet_adoption_api",
    },
    {
        "title": "API Dieta Diária",
        "title_en": "Daily Diet API",
        "description": (
            "API CRUD para registro de refeições e cálculo automático de métricas "
            "nutricionais, com testes automatizados."
        ),
        "description_en": (
            "CRUD API for meal tracking and automatic nutritional metrics, backed "
            "by automated tests."
        ),
        "tags": "Flask, SQLite, Pytest, 95% cobertura",
        "tags_en": "Flask, SQLite, Pytest, 95% coverage",
        "github_url": GITHUB + "daily_diet_api",
    },
    {
        "title": "API de Sistema Bancário",
        "title_en": "Banking System API",
        "description": (
            "API bancária para cadastro, saque e extrato de pessoas físicas e "
            "jurídicas, com regras de negócio validadas por testes."
        ),
        "description_en": (
            "Banking API for customer registration, withdrawals, and statements, "
            "with business rules covered by automated tests."
        ),
        "tags": "Flask, SQLite, Arquitetura MVC, Pytest",
        "tags_en": "Flask, SQLite, MVC Architecture, Pytest",
        "github_url": GITHUB + "banking_system_api",
    },
]

# Projetos que ficam: campo que identifica -> (campos antes, campos depois).
# A Apex é localizada pelo título porque perde a URL: o repositório é privado
# e o botão "Código" levava a um 404.
KEPT_PROJECTS = {
    ("title", "Apex Acelera | Reports"): (
        {
            "order": 4,
            "github_url": GITHUB + "apex-reports",
            "image": "images/projects/apex-reports-overview.png",
        },
        {
            "order": 6,
            "github_url": "",
            # Recorte 920x460 da área das análises, no padrão dos outros previews
            "image": "images/projects/apex-reports.webp",
        },
    ),
    ("github_url", GITHUB + "ecommerce-control"): (
        {"order": 3, "category": "empresarial"},
        {"order": 5, "category": "tecnico"},
    ),
    ("github_url", GITHUB + "atalho-prancheta"): ({"order": 2}, {"order": 4}),
    ("live_url", "https://ibeize.com.br"): ({"order": 1}, {"order": 3}),
    ("github_url", GITHUB + "portfolio_davi_oliveira"): ({"order": 0}, {"order": 2}),
    ("github_url", GITHUB + "python-projects"): (
        {
            "order": 0,
            "image": "",
            "description": (
                "Coleção de APIs, aplicações web, integrações e automações em "
                "Python com boas práticas de arquitetura."
            ),
            "description_en": (
                "Collection of Python APIs, web applications, integrations, and "
                "automations built with sound architecture practices."
            ),
        },
        {
            "order": 1,
            "image": "images/projects/python-projects.webp",
            # Card com imagem pede descrição de até 100 caracteres
            "description": (
                "Coleção de APIs, integrações e automações em Python com boas "
                "práticas de arquitetura."
            ),
            "description_en": (
                "Collection of Python APIs, integrations, and automations built "
                "with sound architecture."
            ),
        },
    ),
    ("github_url", GITHUB + "data_science_projects"): (
        {"order": 0, "image": ""},
        {"order": 0, "image": "images/projects/data-science-projects.webp"},
    ),
}


def _update_kept(apps, alias, state):
    Project = apps.get_model("core", "Project")
    for (key, value), states in KEPT_PROJECTS.items():
        Project.objects.using(alias).filter(**{key: value}).update(**states[state])


def apply_content(apps, schema_editor):
    alias = schema_editor.connection.alias
    Project = apps.get_model("core", "Project")
    Project.objects.using(alias).filter(
        github_url__in=[p["github_url"] for p in REMOVED_PROJECTS]
    ).delete()
    _update_kept(apps, alias, state=1)


def restore_content(apps, schema_editor):
    alias = schema_editor.connection.alias
    Project = apps.get_model("core", "Project")
    for project in REMOVED_PROJECTS:
        Project.objects.using(alias).get_or_create(
            github_url=project["github_url"],
            defaults={**project, "category": "tecnico"},
        )
    _update_kept(apps, alias, state=0)


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0029_match_new_resume"),
    ]

    operations = [
        migrations.RunPython(apply_content, restore_content),
    ]
