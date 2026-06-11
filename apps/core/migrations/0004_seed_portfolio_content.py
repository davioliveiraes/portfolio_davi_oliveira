# Carga inicial do conteúdo do portfólio (antes hardcoded nos templates).
# Conteúdo PT é o campo padrão; EN preenche os campos *_en.

from django.db import migrations

SKILL_CATEGORIES = [
    {
        "name": "Backend & Frameworks",
        "name_en": "Backend & Frameworks",
        "icon": "fas fa-server",
        "skills": [
            ("Python", "", "FastAPI, Flask, Django", "", "fab fa-python"),
            (
                "Go (Golang)",
                "",
                "Em constante evolução",
                "Continuously learning",
                "fab fa-golang",
            ),
            (
                "Design de APIs RESTful",
                "RESTful API Design",
                "",
                "",
                "fas fa-file-code",
            ),
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
        "name": "Frontend",
        "name_en": "Frontend",
        "icon": "fas fa-laptop-code",
        "skills": [
            ("JavaScript", "", "", "", "fab fa-js"),
            ("React.js", "", "", "", "fab fa-react"),
        ],
    },
    {
        "name": "Inteligência Artificial",
        "name_en": "Artificial Intelligence",
        "icon": "fas fa-brain",
        "skills": [
            (
                "Inteligência Artificial & LLMs",
                "Artificial Intelligence & LLMs",
                "",
                "",
                "fas fa-robot",
            ),
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
        "skills": [
            ("Python", "", "", "", "fab fa-python"),
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
        "skills": [
            ("PostgreSQL, MongoDB, SQLite", "", "", "", "fas fa-database"),
            ("SQLAlchemy & ORM", "", "", "", "fas fa-layer-group"),
        ],
    },
    {
        "name": "DevOps & Infra",
        "name_en": "DevOps & Infra",
        "icon": "fas fa-cloud",
        "skills": [
            (
                "Docker & Conteinerização",
                "Docker & Containerization",
                "",
                "",
                "fab fa-docker",
            ),
            ("CI/CD (GitHub Actions)", "", "", "", "fas fa-infinity"),
            (
                "Computação em Nuvem (AWS)",
                "Cloud Computing (AWS)",
                "",
                "",
                "fab fa-aws",
            ),
            (
                "Linux & Linha de Comando",
                "Linux & Command Line",
                "",
                "",
                "fab fa-linux",
            ),
        ],
    },
    {
        "name": "Qualidade & Versionamento",
        "name_en": "Quality & Versioning",
        "icon": "fas fa-tools",
        "skills": [
            (
                "Testes Automatizados (Pytest)",
                "Automated Testing (Pytest)",
                "",
                "",
                "fas fa-vial",
            ),
            (
                "Git & Controle de Versão",
                "Git & Version Control",
                "",
                "",
                "fab fa-git-alt",
            ),
        ],
    },
]

PROJECTS = [
    {
        "title": "API Encurtador de Links",
        "title_en": "URL Shortener API",
        "description": (
            "Sistema de encurtamento de URLs com tracking de cliques e geração de QR "
            "Codes. Interface administrativa para gerenciamento e análise de métricas "
            "de acesso."
        ),
        "description_en": (
            "URL shortening system with click tracking and QR Code generation. "
            "Administrative interface for managing and analyzing access metrics."
        ),
        "tags": "Django REST Framework, PostgreSQL, Docker",
        "github_url": "https://github.com/davioliveiraes/url_shortener_api",
    },
    {
        "title": "API de Sistema Bancário",
        "title_en": "Banking System API",
        "description": (
            "API REST com operações de cadastro, saque e extrato para PF e PJ. Clean "
            "Architecture, testes unitários com Pytest e validações de regras de negócio."
        ),
        "description_en": (
            "REST API with registration, withdrawal, and statement operations for "
            "individuals and companies. Clean Architecture, unit tests with Pytest, "
            "and business-rule validations."
        ),
        "tags": "Flask, SQLite, Arquitetura MVC, Pytest",
        "tags_en": "Flask, SQLite, MVC Architecture, Pytest",
        "github_url": "https://github.com/davioliveiraes/banking_system_api",
    },
    {
        "title": "API Dieta Diária",
        "title_en": "Daily Diet API",
        "description": (
            "API RESTful completa (CRUD) com cálculo automático de métricas "
            "nutricionais. Suite de testes unitários com 95% de cobertura de código."
        ),
        "description_en": (
            "Complete RESTful API (CRUD) with automatic computation of nutritional "
            "metrics. Unit test suite with 95% code coverage."
        ),
        "tags": "Flask, SQLite, Pytest — 95% cobertura",
        "tags_en": "Flask, SQLite, Pytest — 95% coverage",
        "github_url": "https://github.com/davioliveiraes/daily_diet_api",
    },
    {
        "title": "API de Adoção de Pets",
        "title_en": "Pet Adoption API",
        "description": (
            "Aplicação de Clean Architecture e padrão MVC para gestão completa de "
            "adoções. Separação clara de responsabilidades: Controllers, Use Cases, "
            "Repositories."
        ),
        "description_en": (
            "Application of Clean Architecture and the MVC pattern for full adoption "
            "management. Clear separation of responsibilities: Controllers, Use Cases, "
            "Repositories."
        ),
        "tags": "Flask, Clean Architecture, MVC, Pytest",
        "github_url": "https://github.com/davioliveiraes/pet_adoption_api",
    },
    {
        "title": "Chat em Tempo Real",
        "title_en": "Real-Time Chat",
        "description": "Sistema de mensagens instantâneas bidirecionais com WebSockets.",
        "description_en": "Bidirectional instant messaging system using WebSockets.",
        "tags": "Flask-SocketIO, WebSockets",
        "github_url": "https://github.com/davioliveiraes/flask_realtime_chat_socket",
    },
    {
        "title": "API Bancária Segura com JWT",
        "title_en": "JWT Secured Banking API",
        "description": (
            "API REST bancária com autenticação JWT, criptografia de senhas com bcrypt "
            "e middleware de proteção de rotas. Clean Architecture em camadas, padrão "
            "Composer e testes unitários com Pytest."
        ),
        "description_en": (
            "Banking REST API with JWT authentication, bcrypt password hashing and "
            "route-protection middleware. Layered Clean Architecture, Composer pattern "
            "and unit tests with Pytest."
        ),
        "tags": "Flask, PyJWT, bcrypt, SQLite, Pytest",
        "github_url": "https://github.com/davioliveiraes/jwt_secured_banking_api",
    },
    {
        "title": "API de Pedidos com JWT",
        "title_en": "JWT Order API",
        "description": (
            "API REST de pedidos com autenticação e autorização via JWT, onde cada "
            "usuário acessa apenas os próprios dados. Padrão MVC em camadas, injeção "
            "de dependências e cobertura completa de testes unitários."
        ),
        "description_en": (
            "Order REST API with JWT authentication and authorization, where each "
            "user can only access their own data. Layered MVC pattern, dependency "
            "injection and full unit test coverage."
        ),
        "tags": "Flask, PyJWT, bcrypt, SQLite, Pytest",
        "github_url": "https://github.com/davioliveiraes/jwt_order_api",
    },
    {
        "title": "Portfólio Pessoal",
        "title_en": "Personal Portfolio",
        "description": (
            "Site de portfólio profissional com tema dark, Command Palette, formulário "
            "de contato e design responsivo."
        ),
        "description_en": (
            "Professional portfolio website with dark theme, Command Palette, contact "
            "form, and responsive design."
        ),
        "tags": "Python, Django, CSS, JavaScript",
        "github_url": "https://github.com/davioliveiraes/portfolio_davi_oliveira",
        "live_url": "https://davioliveira.tech",
    },
    {
        "title": "Projetos Python",
        "title_en": "Python Projects",
        "description": (
            "Coleção de projetos práticos e exercícios de backend em Python: APIs "
            "RESTful, aplicações web, microserviços, integrações com bancos de dados "
            "e automações, seguindo boas práticas de arquitetura de software."
        ),
        "description_en": (
            "A collection of hands-on backend projects and exercises in Python: "
            "RESTful APIs, web applications, microservices, database integrations and "
            "automations, following software architecture best practices."
        ),
        "tags": "Python, FastAPI, Flask, Django, Docker",
        "github_url": "https://github.com/davioliveiraes/python-projects",
    },
    {
        "title": "Projetos de Ciência de Dados",
        "title_en": "Data Science Projects",
        "description": (
            "Coleção de projetos práticos e exercícios de ciência de dados: análise "
            "exploratória, machine learning, deep learning e análise preditiva "
            "aplicados a problemas reais."
        ),
        "description_en": (
            "A collection of hands-on data science projects and exercises: "
            "exploratory data analysis, machine learning, deep learning and "
            "predictive analytics applied to real-world problems."
        ),
        "tags": "Python, Pandas, Scikit-learn, TensorFlow, Jupyter",
        "github_url": "https://github.com/davioliveiraes/data_science_projects",
    },
]

EXPERIENCES = [
    {
        "role": "Analista de E-commerce",
        "role_en": "E-commerce Analyst",
        "company": "iBeize",
        "company_url": "https://www.ibeize.com.br",
        "period": "Fev 2026 - Presente · Morada Nova, CE · Presencial",
        "period_en": "Feb 2026 - Present · Morada Nova, CE · On-site",
        "details": (
            "Análise de resultados, experimentação e otimizações contínuas da loja NuvemShop\n"
            "Customização do storefront via CSS/HTML/JS/GoTemplate avançado e integração com ERP GestãoClick\n"
            "Monitoramento de KPIs, testes de performance e otimização de ROI\n"
            "Configuração de DNS, integração com Melhor Envio e alinhamento de SKUs com estoque\n"
            "Desenvolvimento do Ibeize Ecommerce Control — sistema interno fullstack (Django Ninja + React + Docker) para gestão de catálogo e finanças\n"
            "Suporte em ações comerciais e integração com operação logística"
        ),
        "details_en": (
            "Results analysis, experimentation, and continuous optimizations for the NuvemShop store\n"
            "Storefront customization via advanced CSS/HTML/JS/GoTemplate and integration with GestãoClick ERP\n"
            "KPI monitoring, performance testing, and ROI optimization\n"
            "DNS configuration, integration with Melhor Envio, and SKU alignment with inventory\n"
            "Development of Ibeize Ecommerce Control — internal fullstack system (Django Ninja + React + Docker) for catalog and finance management\n"
            "Support for commercial actions and integration with logistics operations"
        ),
        "skills": "NuvemShop, GestãoClick, CSS, HTML, JavaScript, GoTemplate, Django Ninja, React, Docker, KPIs, ROI, DNS, Melhor Envio",
        "skills_en": "NuvemShop, GestãoClick, CSS, HTML, JavaScript, GoTemplate, Django Ninja, React, Docker, KPIs, ROI, DNS, Melhor Envio",
    },
    {
        "role": "Assistente Administrativo",
        "role_en": "Administrative Assistant",
        "company": "Hiper Morada Nova",
        "period": "2021 - 2025 · Morada Nova, CE · Presencial",
        "period_en": "2021 - 2025 · Morada Nova, CE · On-site",
        "details": (
            "Desenvolvi dashboards automatizados em Excel, transformando dados brutos em insights de negócio\n"
            "Otimizei relatórios internos com lógica de processamento que reduziu o tempo de geração em até 60%\n"
            "Automatizei análises e relatórios administrativos, melhorando a precisão e eficiência operacional\n"
            "Prestei suporte técnico a sistemas e equipamentos, garantindo a continuidade operacional do SysPDV"
        ),
        "details_en": (
            "Built automated Excel dashboards, turning raw data into business insights\n"
            "Optimized internal reports with processing logic that reduced generation time by up to 60%\n"
            "Automated administrative analyses and reports, improving accuracy and operational efficiency\n"
            "Provided technical support for systems and equipment, ensuring operational continuity of SysPDV"
        ),
        "skills": "Excel, Dashboards, Automação de Relatórios, SysPDV, Suporte Técnico",
        "skills_en": "Excel, Dashboards, Report Automation, SysPDV, Technical Support",
    },
    {
        "role": "Jovem Aprendiz",
        "role_en": "Young Apprentice",
        "company": "Betânia Lácteos",
        "period": "2020 - 2021 · Morada Nova, CE · Presencial",
        "period_en": "2020 - 2021 · Morada Nova, CE · On-site",
        "details": (
            "Organizei documentação fiscal e planilhas administrativas, aprimorando o controle de dados\n"
            "Desenvolvi atenção a detalhes e precisão em registros administrativos"
        ),
        "details_en": (
            "Organized fiscal documentation and administrative spreadsheets, improving data control\n"
            "Developed attention to detail and accuracy in administrative records"
        ),
        "skills": "Documentação Fiscal, Planilhas Administrativas, Controle de Dados",
        "skills_en": "Tax Documentation, Administrative Spreadsheets, Data Control",
    },
    {
        "role": "Estagiário",
        "role_en": "Intern",
        "company": "Prisma Informática",
        "period": "2017 · Morada Nova, CE · Presencial",
        "period_en": "2017 · Morada Nova, CE · On-site",
        "details": (
            "Iniciei contato com desenvolvimento web (HTML5, CSS3 e JavaScript)\n"
            "Ofereci suporte técnico e atendimento a clientes, fortalecendo comunicação e resolução de problemas"
        ),
        "details_en": (
            "Started working with web development (HTML5, CSS3, and JavaScript)\n"
            "Provided technical support and customer service, strengthening communication and problem-solving skills"
        ),
        "skills": "HTML5, CSS3, JavaScript, Suporte Técnico, Atendimento ao Cliente",
        "skills_en": "HTML5, CSS3, JavaScript, Technical Support, Customer Service",
    },
]

CERTIFICATIONS = [
    (
        "Arquitetura de Software e Padrão MVC",
        "Software Architecture and MVC Pattern",
        "Rocketseat",
        10,
    ),
    (
        "Design do Código — SOLID e Testes",
        "Code Design — SOLID and Testing",
        "Rocketseat",
        6,
    ),
    ("Explorando Flask", "Exploring Flask", "Rocketseat", 10),
    ("Fundamentos de Python", "Python Fundamentals", "Rocketseat", 10),
    ("Python 3 Completo", "Complete Python 3", "Curso em Vídeo", 80),
    (
        "Imersão Build & Automate — Desenvolvimento e Automação com IA",
        "Build & Automate Immersion — Development and Automation with AI",
        "Rocketseat",
        5,
    ),
    (
        "Logic Master — Lógica de Programação e Algoritmos com Python",
        "Logic Master — Programming Logic and Algorithms with Python",
        "PyCodeBR Treinamentos",
        5,
    ),
    (
        "Autenticação JWT e Segurança",
        "JWT Authentication and Security",
        "Rocketseat",
        7,
    ),
]


def seed(apps, schema_editor):
    SkillCategory = apps.get_model("core", "SkillCategory")
    Skill = apps.get_model("core", "Skill")
    Project = apps.get_model("core", "Project")
    Experience = apps.get_model("core", "Experience")
    Certification = apps.get_model("core", "Certification")

    for cat_order, cat in enumerate(SKILL_CATEGORIES):
        category = SkillCategory.objects.create(
            name=cat["name"], name_en=cat["name_en"], icon=cat["icon"], order=cat_order
        )
        for skill_order, (name, name_en, detail, detail_en, icon) in enumerate(
            cat["skills"]
        ):
            Skill.objects.create(
                category=category,
                name=name,
                name_en=name_en,
                detail=detail,
                detail_en=detail_en,
                icon=icon,
                order=skill_order,
            )

    for order, project in enumerate(PROJECTS):
        Project.objects.create(order=order, **project)

    for order, experience in enumerate(EXPERIENCES):
        Experience.objects.create(order=order, **experience)

    for order, (name, name_en, institution, hours) in enumerate(CERTIFICATIONS):
        Certification.objects.create(
            name=name,
            name_en=name_en,
            institution=institution,
            hours=hours,
            order=order,
        )


def unseed(apps, schema_editor):
    for model_name in [
        "Skill",
        "SkillCategory",
        "Project",
        "Experience",
        "Certification",
    ]:
        apps.get_model("core", model_name).objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_certification_experience_project_skillcategory_skill"),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
