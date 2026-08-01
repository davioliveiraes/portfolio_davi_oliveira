# Redesign v2 (Nocturne): regra de copywriting sem travessões e chips de
# skills alinhados ao protótipo (um chip por tecnologia).
#
# - Períodos por extenso: "Fev 2026 até hoje", "2021 a 2025" (EN: "to today",
#   "2021 to 2025"), sem o sufixo "Presencial".
# - Certificações com dois-pontos no lugar do travessão.
# - Descrição do Ecommerce Control e tags da API Dieta Diária sem travessão.
# - Skills: divide "PostgreSQL, MongoDB, SQLite", encurta nomes longos e
#   adiciona Django, FastAPI, Flask, Nginx + Gunicorn, Pre-commit, Black & isort.

from django.db import migrations

# (empresa, período novo PT, período novo EN, período antigo PT, período antigo EN)
PERIODS = [
    (
        "iBeize",
        "Fev 2026 até hoje · Morada Nova, CE",
        "Feb 2026 to today · Morada Nova, CE",
        "Fev 2026 - Presente · Morada Nova, CE · Presencial",
        "Feb 2026 - Present · Morada Nova, CE · On-site",
    ),
    (
        "Hiper Morada Nova",
        "2021 a 2025 · Morada Nova, CE",
        "2021 to 2025 · Morada Nova, CE",
        "2021 - 2025 · Morada Nova, CE · Presencial",
        "2021 - 2025 · Morada Nova, CE · On-site",
    ),
    (
        "Betânia Lácteos",
        "2020 a 2021 · Morada Nova, CE",
        "2020 to 2021 · Morada Nova, CE",
        "2020 - 2021 · Morada Nova, CE · Presencial",
        "2020 - 2021 · Morada Nova, CE · On-site",
    ),
    (
        "Prisma Informática",
        "2017 · Morada Nova, CE",
        "2017 · Morada Nova, CE",
        "2017 · Morada Nova, CE · Presencial",
        "2017 · Morada Nova, CE · On-site",
    ),
]

# (nome antigo, nome novo, nome_en antigo, nome_en novo)
CERTS = [
    (
        "Design do Código — SOLID e Testes",
        "Design do Código: SOLID e Testes",
        "Code Design — SOLID and Testing",
        "Code Design: SOLID and Testing",
    ),
    (
        "Imersão Build & Automate — Desenvolvimento e Automação com IA",
        "Imersão Build & Automate: desenvolvimento e automação com IA",
        "Build & Automate Immersion — Development and Automation with AI",
        "Build & Automate Immersion: development and automation with AI",
    ),
    (
        "Logic Master — Lógica de Programação e Algoritmos com Python",
        "Logic Master: lógica de programação e algoritmos com Python",
        "Logic Master — Programming Logic and Algorithms with Python",
        "Logic Master: programming logic and algorithms with Python",
    ),
]

ECOMMERCE_DESC = {
    "old": (
        "Painel de controle multi-tenant para lojistas Nuvemshop + GestãoClick "
        "— catálogo, financeiro e relatórios em PDF em um só lugar. Cada "
        "empresa cria sua conta e enxerga apenas os próprios dados."
    ),
    "new": (
        "Painel de controle multi-tenant para lojistas Nuvemshop + GestãoClick: "
        "catálogo, financeiro e relatórios em PDF em um só lugar. Cada "
        "empresa cria sua conta e enxerga apenas os próprios dados."
    ),
    "old_en": (
        "Multi-tenant control panel for Nuvemshop + GestãoClick merchants — "
        "catalog, finance and PDF reports in one place. Each company creates "
        "its own account and sees only its own data."
    ),
    "new_en": (
        "Multi-tenant control panel for Nuvemshop + GestãoClick merchants: "
        "catalog, finance and PDF reports in one place. Each company creates "
        "its own account and sees only its own data."
    ),
}

DIETA_TAGS = {
    "old": "Flask, SQLite, Pytest — 95% cobertura",
    "new": "Flask, SQLite, Pytest, 95% cobertura",
    "old_en": "Flask, SQLite, Pytest — 95% coverage",
    "new_en": "Flask, SQLite, Pytest, 95% coverage",
}

# (categoria, nome antigo, nome novo, name_en antigo, name_en novo)
SKILL_RENAMES = [
    (
        "Inteligência Artificial",
        "Inteligência Artificial & LLMs",
        "LLMs",
        "Artificial Intelligence & LLMs",
        "",
    ),
    (
        "Backend & Frameworks",
        "Design de APIs RESTful",
        "APIs RESTful",
        "RESTful API Design",
        "RESTful APIs",
    ),
    (
        "DevOps & Infra",
        "Docker & Conteinerização",
        "Docker",
        "Docker & Containerization",
        "",
    ),
    ("DevOps & Infra", "Computação em Nuvem (AWS)", "AWS", "Cloud Computing (AWS)", ""),
    (
        "DevOps & Infra",
        "Linux & Linha de Comando",
        "Linux & CLI",
        "Linux & Command Line",
        "",
    ),
    (
        "Qualidade & Versionamento",
        "Testes Automatizados (Pytest)",
        "Pytest",
        "Automated Testing (Pytest)",
        "",
    ),
    (
        "Qualidade & Versionamento",
        "Git & Controle de Versão",
        "Git",
        "Git & Version Control",
        "",
    ),
]

# (categoria, nome, ordem) — chips novos do protótipo
SKILL_ADDITIONS = [
    ("Backend & Frameworks", "Django", 1),
    ("Backend & Frameworks", "FastAPI", 2),
    ("Backend & Frameworks", "Flask", 3),
    ("DevOps & Infra", "Nginx + Gunicorn", 4),
    ("Qualidade & Versionamento", "Pre-commit", 2),
    ("Qualidade & Versionamento", "Black & isort", 3),
]

# Ordem final do grupo Backend (chips novos intercalados)
BACKEND_ORDER = [
    ("Python", 0),
    ("Django", 1),
    ("FastAPI", 2),
    ("Flask", 3),
    ("Go (Golang)", 4),
    ("APIs RESTful", 5),
    ("Clean Architecture & MVC", 6),
    ("Integração de serviços externos", 7),
]


def apply(apps, schema_editor):
    Experience = apps.get_model("core", "Experience")
    Certification = apps.get_model("core", "Certification")
    Project = apps.get_model("core", "Project")
    Skill = apps.get_model("core", "Skill")
    SkillCategory = apps.get_model("core", "SkillCategory")

    for company, new_pt, new_en, _old_pt, _old_en in PERIODS:
        Experience.objects.filter(company=company).update(
            period=new_pt, period_en=new_en
        )

    for old, new, _old_en, new_en in CERTS:
        Certification.objects.filter(name=old).update(name=new, name_en=new_en)

    Project.objects.filter(title="Ecommerce Control").update(
        description=ECOMMERCE_DESC["new"], description_en=ECOMMERCE_DESC["new_en"]
    )
    Project.objects.filter(title="API Dieta Diária").update(
        tags=DIETA_TAGS["new"], tags_en=DIETA_TAGS["new_en"]
    )

    for cat_name, old, new, _old_en, new_en in SKILL_RENAMES:
        Skill.objects.filter(category__name=cat_name, name=old).update(
            name=new, name_en=new_en
        )

    # Divide o chip triplo de bancos de dados em três
    db_cat = SkillCategory.objects.filter(name="Banco de Dados").first()
    if db_cat:
        triple = Skill.objects.filter(
            category=db_cat, name="PostgreSQL, MongoDB, SQLite"
        ).first()
        if triple:
            triple.name = "PostgreSQL"
            triple.name_en = ""
            triple.order = 0
            triple.save()
            Skill.objects.get_or_create(
                category=db_cat,
                name="MongoDB",
                defaults={"icon": triple.icon, "order": 1},
            )
            Skill.objects.get_or_create(
                category=db_cat,
                name="SQLite",
                defaults={"icon": triple.icon, "order": 2},
            )
            Skill.objects.filter(category=db_cat, name="SQLAlchemy & ORM").update(
                order=3
            )

    # Python duplicado no grupo Dados sai (o protótipo lista só as libs)
    Skill.objects.filter(category__name="Dados", name="Python").delete()

    for cat_name, name, order in SKILL_ADDITIONS:
        cat = SkillCategory.objects.filter(name=cat_name).first()
        if cat and not Skill.objects.filter(category=cat, name=name).exists():
            Skill.objects.create(category=cat, name=name, icon="", order=order)

    backend = SkillCategory.objects.filter(name="Backend & Frameworks").first()
    if backend:
        for name, order in BACKEND_ORDER:
            Skill.objects.filter(category=backend, name=name).update(order=order)


def revert(apps, schema_editor):
    Experience = apps.get_model("core", "Experience")
    Certification = apps.get_model("core", "Certification")
    Project = apps.get_model("core", "Project")
    Skill = apps.get_model("core", "Skill")
    SkillCategory = apps.get_model("core", "SkillCategory")

    for company, _new_pt, _new_en, old_pt, old_en in PERIODS:
        Experience.objects.filter(company=company).update(
            period=old_pt, period_en=old_en
        )

    for old, new, old_en, _new_en in CERTS:
        Certification.objects.filter(name=new).update(name=old, name_en=old_en)

    Project.objects.filter(title="Ecommerce Control").update(
        description=ECOMMERCE_DESC["old"], description_en=ECOMMERCE_DESC["old_en"]
    )
    Project.objects.filter(title="API Dieta Diária").update(
        tags=DIETA_TAGS["old"], tags_en=DIETA_TAGS["old_en"]
    )

    for cat_name, name, _order in SKILL_ADDITIONS:
        Skill.objects.filter(category__name=cat_name, name=name).delete()

    for cat_name, old, new, old_en, _new_en in SKILL_RENAMES:
        Skill.objects.filter(category__name=cat_name, name=new).update(
            name=old, name_en=old_en
        )

    db_cat = SkillCategory.objects.filter(name="Banco de Dados").first()
    if db_cat:
        Skill.objects.filter(category=db_cat, name__in=["MongoDB", "SQLite"]).delete()
        Skill.objects.filter(category=db_cat, name="PostgreSQL").update(
            name="PostgreSQL, MongoDB, SQLite", order=0
        )
        Skill.objects.filter(category=db_cat, name="SQLAlchemy & ORM").update(order=1)

    dados = SkillCategory.objects.filter(name="Dados").first()
    if dados and not Skill.objects.filter(category=dados, name="Python").exists():
        Skill.objects.create(category=dados, name="Python", icon="", order=0)


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0010_reorder_projects_by_date"),
    ]

    operations = [
        migrations.RunPython(apply, revert),
    ]
