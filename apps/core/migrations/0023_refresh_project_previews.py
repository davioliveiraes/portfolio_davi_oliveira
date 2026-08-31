# Atualiza o nome e a imagem do Apex Reports e transforma todas as descrições
# em previews curtos, completos e sem reticências.

from django.db import migrations

PROJECT_COPY = [
    {
        "old_title": "Apex Reports",
        "old_title_en": "Apex Reports",
        "title": "Apex Acelera | Reports",
        "title_en": "Apex Acelera | Reports",
        "old_description": (
            "Gerador de relatórios em PDF a partir de exports do Meta Ads Manager, "
            "com quatro modos de saída, cálculo de KPIs e deploy em VPS (Nginx, "
            "Gunicorn, systemd)."
        ),
        "description": (
            "Gerador de relatórios em PDF para dados do Meta Ads, com quatro modos "
            "de análise e cálculo automático de KPIs."
        ),
        "old_description_en": (
            "PDF report generator built from Meta Ads Manager exports, with four "
            "output modes, KPI calculation and VPS deploy (Nginx, Gunicorn, systemd)."
        ),
        "description_en": (
            "PDF report generator for Meta Ads data, with four analysis modes and "
            "automatic KPI calculation."
        ),
        "image": "images/projects/apex-reports.png",
        "old_image": "images/projects/apex-reports.webp",
    },
    {
        "old_title": "Ecommerce Control",
        "title": "Ecommerce Control",
        "title_en": "Ecommerce Control",
        "old_description": (
            "Painel de controle multi-tenant para lojistas Nuvemshop + GestãoClick: "
            "catálogo, financeiro e relatórios em PDF em um só lugar. Cada empresa "
            "cria sua conta e enxerga apenas os próprios dados."
        ),
        "description": (
            "Painel multi-tenant que integra Nuvemshop e GestãoClick para centralizar "
            "catálogo, financeiro e relatórios em PDF."
        ),
        "old_description_en": (
            "Multi-tenant control panel for Nuvemshop + GestãoClick merchants: "
            "catalog, finance and PDF reports in one place. Each company creates its "
            "own account and sees only its own data."
        ),
        "description_en": (
            "Multi-tenant dashboard integrating Nuvemshop and GestãoClick to "
            "centralize catalog, finance, and PDF reports."
        ),
    },
    {
        "old_title": "E-commerce Ibeize",
        "title": "E-commerce Ibeize",
        "title_en": "Ibeize E-commerce",
        "old_description": (
            "Integração com o ERP GestãoClick e customização do storefront via "
            "GoTemplate no back-end da loja NuvemShop. Análise de resultados, "
            "experimentação e otimizações contínuas. Configuração de DNS, integração "
            "com Melhor Envio e alinhamento de SKUs com o estoque."
        ),
        "description": (
            "E-commerce integrado ao GestãoClick, com storefront em GoTemplate, "
            "logística via Melhor Envio e estoque sincronizado."
        ),
        "old_description_en": (
            "Integration with the GestãoClick ERP and storefront customization via "
            "GoTemplate on the NuvemShop store's back end. Results analysis, "
            "experimentation, and continuous optimizations. DNS configuration, "
            "Melhor Envio integration, and SKU alignment with inventory."
        ),
        "description_en": (
            "E-commerce integrated with GestãoClick, featuring a GoTemplate "
            "storefront, Melhor Envio shipping, and synchronized inventory."
        ),
    },
    {
        "old_title": "Projetos de Ciência de Dados",
        "title": "Projetos de Ciência de Dados",
        "title_en": "Data Science Projects",
        "old_description": (
            "Coleção de projetos práticos e exercícios de ciência de dados: análise "
            "exploratória, machine learning, deep learning e análise preditiva "
            "aplicados a problemas reais."
        ),
        "description": (
            "Coleção de análises exploratórias e modelos de machine learning "
            "aplicados a problemas reais."
        ),
        "old_description_en": (
            "A collection of hands-on data science projects and exercises: "
            "exploratory data analysis, machine learning, deep learning and "
            "predictive analytics applied to real-world problems."
        ),
        "description_en": (
            "Collection of exploratory analyses and machine-learning models applied "
            "to real-world problems."
        ),
    },
    {
        "old_title": "Projetos Python",
        "title": "Projetos Python",
        "title_en": "Python Projects",
        "old_description": (
            "Coleção de projetos práticos e exercícios de backend em Python: APIs "
            "RESTful, aplicações web, microserviços, integrações com bancos de dados "
            "e automações, seguindo boas práticas de arquitetura de software."
        ),
        "description": (
            "Coleção de APIs, aplicações web, integrações e automações em Python com "
            "boas práticas de arquitetura."
        ),
        "old_description_en": (
            "A collection of hands-on backend projects and exercises in Python: "
            "RESTful APIs, web applications, microservices, database integrations "
            "and automations, following software architecture best practices."
        ),
        "description_en": (
            "Collection of Python APIs, web applications, integrations, and "
            "automations built with sound architecture practices."
        ),
    },
    {
        "old_title": "Portfólio Pessoal",
        "title": "Portfólio Pessoal",
        "title_en": "Personal Portfolio",
        "old_description": (
            "Site de portfólio profissional com tema dark, Command Palette, "
            "formulário de contato e design responsivo."
        ),
        "description": (
            "Portfólio profissional bilíngue em Django, com temas claro e escuro, "
            "busca rápida, contato e design responsivo."
        ),
        "old_description_en": (
            "Professional portfolio website with dark theme, Command Palette, "
            "contact form, and responsive design."
        ),
        "description_en": (
            "Bilingual professional portfolio built with Django, featuring light and "
            "dark themes, quick search, contact form, and responsive design."
        ),
    },
    {
        "old_title": "API de Pedidos com JWT",
        "title": "API de Pedidos com JWT",
        "title_en": "JWT Order API",
        "old_description": (
            "API REST de pedidos com autenticação e autorização via JWT, onde cada "
            "usuário acessa apenas os próprios dados. Padrão MVC em camadas, injeção "
            "de dependências e cobertura completa de testes unitários."
        ),
        "description": (
            "API de pedidos com autenticação JWT, isolamento de dados por usuário, "
            "arquitetura em camadas e testes automatizados."
        ),
        "old_description_en": (
            "Order REST API with JWT authentication and authorization, where each "
            "user can only access their own data. Layered MVC pattern, dependency "
            "injection and full unit test coverage."
        ),
        "description_en": (
            "Order API with JWT authentication, per-user data isolation, layered "
            "architecture, and automated tests."
        ),
    },
    {
        "old_title": "API Bancária Segura com JWT",
        "title": "API Bancária Segura com JWT",
        "title_en": "JWT Secured Banking API",
        "old_description": (
            "API REST bancária com autenticação JWT, criptografia de senhas com "
            "bcrypt e middleware de proteção de rotas. Clean Architecture em "
            "camadas, padrão Composer e testes unitários com Pytest."
        ),
        "description": (
            "API bancária com autenticação JWT, senhas protegidas por bcrypt, "
            "arquitetura em camadas e testes automatizados."
        ),
        "old_description_en": (
            "Banking REST API with JWT authentication, bcrypt password hashing and "
            "route-protection middleware. Layered Clean Architecture, Composer "
            "pattern and unit tests with Pytest."
        ),
        "description_en": (
            "Banking API with JWT authentication, bcrypt password protection, "
            "layered architecture, and automated tests."
        ),
    },
    {
        "old_title": "Chat em Tempo Real",
        "title": "Chat em Tempo Real",
        "title_en": "Real-Time Chat",
        "old_description": (
            "Sistema de mensagens instantâneas bidirecionais com WebSockets."
        ),
        "description": (
            "Sistema de mensagens bidirecionais em tempo real desenvolvido com "
            "WebSockets."
        ),
        "old_description_en": (
            "Bidirectional instant messaging system using WebSockets."
        ),
        "description_en": (
            "Real-time bidirectional messaging system built with WebSockets."
        ),
    },
    {
        "old_title": "API de Adoção de Pets",
        "title": "API de Adoção de Pets",
        "title_en": "Pet Adoption API",
        "old_description": (
            "Aplicação de Clean Architecture e padrão MVC para gestão completa de "
            "adoções. Separação clara de responsabilidades: Controllers, Use Cases, "
            "Repositories."
        ),
        "description": (
            "API para gestão de adoções de pets, estruturada com Clean Architecture, "
            "MVC e separação entre casos de uso e repositórios."
        ),
        "old_description_en": (
            "Application of Clean Architecture and the MVC pattern for full "
            "adoption management. Clear separation of responsibilities: Controllers, "
            "Use Cases, Repositories."
        ),
        "description_en": (
            "Pet adoption management API structured with Clean Architecture, MVC, "
            "and separated use cases and repositories."
        ),
    },
    {
        "old_title": "API Dieta Diária",
        "title": "API Dieta Diária",
        "title_en": "Daily Diet API",
        "old_description": (
            "API RESTful completa (CRUD) com cálculo automático de métricas "
            "nutricionais. Suite de testes unitários com 95% de cobertura de código."
        ),
        "description": (
            "API CRUD para registro de refeições e cálculo automático de métricas "
            "nutricionais, com testes automatizados."
        ),
        "old_description_en": (
            "Complete RESTful API (CRUD) with automatic computation of nutritional "
            "metrics. Unit test suite with 95% code coverage."
        ),
        "description_en": (
            "CRUD API for meal tracking and automatic nutritional metrics, backed by "
            "automated tests."
        ),
    },
    {
        "old_title": "API de Sistema Bancário",
        "title": "API de Sistema Bancário",
        "title_en": "Banking System API",
        "old_description": (
            "API REST com operações de cadastro, saque e extrato para PF e PJ. Clean "
            "Architecture, testes unitários com Pytest e validações de regras de negócio."
        ),
        "description": (
            "API bancária para cadastro, saque e extrato de pessoas físicas e "
            "jurídicas, com regras de negócio validadas por testes."
        ),
        "old_description_en": (
            "REST API with registration, withdrawal, and statement operations for "
            "individuals and companies. Clean Architecture, unit tests with Pytest, "
            "and business-rule validations."
        ),
        "description_en": (
            "Banking API for customer registration, withdrawals, and statements, "
            "with business rules covered by automated tests."
        ),
    },
    {
        "old_title": "API Encurtador de Links",
        "title": "API Encurtador de Links",
        "title_en": "URL Shortener API",
        "old_description": (
            "Sistema de encurtamento de URLs com tracking de cliques e geração de QR "
            "Codes. Interface administrativa para gerenciamento e análise de métricas "
            "de acesso."
        ),
        "description": (
            "Encurtador de URLs com rastreamento de cliques, geração de QR Codes e "
            "painel administrativo de métricas."
        ),
        "old_description_en": (
            "URL shortening system with click tracking and QR Code generation. "
            "Administrative interface for managing and analyzing access metrics."
        ),
        "description_en": (
            "URL shortener with click tracking, QR Code generation, and an "
            "administrative metrics dashboard."
        ),
    },
]


def apply_copy(apps, schema_editor):
    Project = apps.get_model("core", "Project")
    for copy in PROJECT_COPY:
        updates = {
            "title": copy["title"],
            "title_en": copy["title_en"],
            "description": copy["description"],
            "description_en": copy["description_en"],
        }
        if "image" in copy:
            updates["image"] = copy["image"]
        Project.objects.filter(title=copy["old_title"]).update(**updates)


def revert_copy(apps, schema_editor):
    Project = apps.get_model("core", "Project")
    for copy in reversed(PROJECT_COPY):
        updates = {
            "title": copy["old_title"],
            "description": copy["old_description"],
            "description_en": copy["old_description_en"],
        }
        if "old_title_en" in copy:
            updates["title_en"] = copy["old_title_en"]
        if "old_image" in copy:
            updates["image"] = copy["old_image"]
        Project.objects.filter(title=copy["title"]).update(**updates)


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0022_apex_acelera_data_role"),
    ]

    operations = [
        migrations.RunPython(apply_copy, revert_copy),
    ]
