# Reposiciona o portfólio para Programação, Sistemas, APIs, Backend e Dados,
# removendo menções a frontend (categoria de skills, tags de projeto e
# trechos de experiência que citavam CSS/HTML/JS/React/TypeScript).

from django.db import migrations

FRONTEND_CATEGORY_NAME = "Frontend"

FRONTEND_SKILLS = [
    {"name": "JavaScript", "icon": "fab fa-js", "order": 0},
    {"name": "TypeScript", "icon": "icon-ts", "order": 1},
    {"name": "React.js", "icon": "fab fa-react", "order": 2},
]

PROJECT_TAGS = {
    "Ecommerce Control": (
        "Django Ninja, PostgreSQL, Docker, JWT",
        "",
    ),
    "E-commerce Ibeize": (
        "NuvemShop, GoTemplate, GestãoClick, Integração de API",
        "",
    ),
    "Portfólio Pessoal": (
        "Python, Django, PostgreSQL, Deploy VPS",
        "",
    ),
}

OLD_PROJECT_TAGS = {
    "Ecommerce Control": (
        "Django Ninja, React, TypeScript, PostgreSQL, Docker",
        "",
    ),
    "E-commerce Ibeize": (
        "NuvemShop, GoTemplate, JavaScript, GestãoClick",
        "",
    ),
    "Portfólio Pessoal": (
        "Python, Django, CSS, JavaScript",
        "",
    ),
}

IBEIZE_DESCRIPTION = (
    "Integração com o ERP GestãoClick e customização do storefront via "
    "GoTemplate no back-end da loja NuvemShop. Análise de resultados, "
    "experimentação e otimizações contínuas. Configuração de DNS, integração "
    "com Melhor Envio e alinhamento de SKUs com o estoque."
)
IBEIZE_DESCRIPTION_EN = (
    "Integration with the GestãoClick ERP and storefront customization via "
    "GoTemplate on the NuvemShop store's back end. Results analysis, "
    "experimentation, and continuous optimizations. DNS configuration, "
    "Melhor Envio integration, and SKU alignment with inventory."
)

OLD_IBEIZE_DESCRIPTION = (
    "Customização do storefront via CSS/HTML/JS/GoTemplate avançado e "
    "integração com ERP GestãoClick. Análise de resultados, experimentação e "
    "otimizações contínuas da loja NuvemShop. Configuração de DNS, integração "
    "com Melhor Envio e alinhamento de SKUs com estoque."
)
OLD_IBEIZE_DESCRIPTION_EN = (
    "Storefront customization with advanced CSS/HTML/JS/GoTemplate and "
    "integration with the GestãoClick ERP. Results analysis, experimentation "
    "and continuous optimizations of the NuvemShop store. DNS setup, Melhor "
    "Envio shipping integration and SKU alignment with inventory."
)

IBEIZE_SKILLS = (
    "NuvemShop, GestãoClick, GoTemplate, Django Ninja, Docker, KPIs, ROI, "
    "DNS, Melhor Envio"
)
IBEIZE_SKILLS_EN = IBEIZE_SKILLS
OLD_IBEIZE_SKILLS = (
    "NuvemShop, GestãoClick, CSS, HTML, JavaScript, GoTemplate, Django Ninja, "
    "React, Docker, KPIs, ROI, DNS, Melhor Envio"
)

IBEIZE_DETAILS = (
    "Análise de resultados, experimentação e otimizações contínuas da loja "
    "NuvemShop\n"
    "Integração com o ERP GestãoClick e customização do storefront via "
    "GoTemplate\n"
    "Configuração de DNS, integração com Melhor Envio e alinhamento de SKUs "
    "com o estoque, apoiando ações comerciais e a operação logística"
)
IBEIZE_DETAILS_EN = (
    "Results analysis, experimentation, and continuous optimizations for the "
    "NuvemShop store\n"
    "Integration with the GestãoClick ERP and storefront customization via "
    "GoTemplate\n"
    "DNS configuration, Melhor Envio integration, and SKU alignment with "
    "inventory, supporting commercial actions and logistics operations"
)

OLD_IBEIZE_DETAILS = (
    "Análise de resultados, experimentação e otimizações contínuas da loja "
    "NuvemShop\n"
    "Customização do storefront via CSS/HTML/JS/GoTemplate avançado e "
    "integração com o ERP GestãoClick\n"
    "Configuração de DNS, integração com Melhor Envio e alinhamento de SKUs "
    "com o estoque, apoiando ações comerciais e a operação logística"
)
OLD_IBEIZE_DETAILS_EN = (
    "Results analysis, experimentation, and continuous optimizations for the "
    "NuvemShop store\n"
    "Storefront customization via advanced CSS/HTML/JS/GoTemplate and "
    "integration with the GestãoClick ERP\n"
    "DNS configuration, Melhor Envio integration, and SKU alignment with "
    "inventory, supporting commercial actions and logistics operations"
)

PRISMA_SKILLS = "Lógica de Programação, Suporte Técnico, Atendimento ao Cliente"
OLD_PRISMA_SKILLS = "HTML5, CSS3, JavaScript, Suporte Técnico, Atendimento ao Cliente"

PRISMA_SKILLS_EN = "Programming Logic, Technical Support, Customer Service"
OLD_PRISMA_SKILLS_EN = "HTML5, CSS3, JavaScript, Technical Support, Customer Service"

PRISMA_DETAILS = (
    "Iniciei contato com programação e lógica de desenvolvimento de sistemas\n"
    "Ofereci suporte técnico e atendimento a clientes, fortalecendo "
    "comunicação e resolução de problemas\n"
    "Auxiliei na manutenção e configuração de computadores e periféricos, "
    "acompanhando os chamados até a resolução"
)
PRISMA_DETAILS_EN = (
    "Started working with programming and systems development logic\n"
    "Provided technical support and customer service, strengthening "
    "communication and problem-solving skills\n"
    "Assisted with the maintenance and setup of computers and peripherals, "
    "following tickets through to resolution"
)

OLD_PRISMA_DETAILS = (
    "Iniciei contato com desenvolvimento web (HTML5, CSS3 e JavaScript)\n"
    "Ofereci suporte técnico e atendimento a clientes, fortalecendo "
    "comunicação e resolução de problemas\n"
    "Auxiliei na manutenção e configuração de computadores e periféricos, "
    "acompanhando os chamados até a resolução"
)
OLD_PRISMA_DETAILS_EN = (
    "Started working with web development (HTML5, CSS3, and JavaScript)\n"
    "Provided technical support and customer service, strengthening "
    "communication and problem-solving skills\n"
    "Assisted with the maintenance and setup of computers and peripherals, "
    "following tickets through to resolution"
)


def set_project_tags(Project, mapping):
    for title, (tags, tags_en) in mapping.items():
        Project.objects.filter(title=title).update(tags=tags, tags_en=tags_en)


def apply_changes(apps, schema_editor):
    SkillCategory = apps.get_model("core", "SkillCategory")
    Project = apps.get_model("core", "Project")
    Experience = apps.get_model("core", "Experience")

    SkillCategory.objects.filter(name=FRONTEND_CATEGORY_NAME).delete()

    set_project_tags(Project, PROJECT_TAGS)
    Project.objects.filter(title="E-commerce Ibeize").update(
        description=IBEIZE_DESCRIPTION,
        description_en=IBEIZE_DESCRIPTION_EN,
    )

    Experience.objects.filter(company="iBeize").update(
        skills=IBEIZE_SKILLS,
        skills_en=IBEIZE_SKILLS_EN,
        details=IBEIZE_DETAILS,
        details_en=IBEIZE_DETAILS_EN,
    )

    Experience.objects.filter(company="Prisma Informática").update(
        skills=PRISMA_SKILLS,
        skills_en=PRISMA_SKILLS_EN,
        details=PRISMA_DETAILS,
        details_en=PRISMA_DETAILS_EN,
    )


def revert_changes(apps, schema_editor):
    SkillCategory = apps.get_model("core", "SkillCategory")
    Skill = apps.get_model("core", "Skill")
    Project = apps.get_model("core", "Project")
    Experience = apps.get_model("core", "Experience")

    category = SkillCategory.objects.create(
        name=FRONTEND_CATEGORY_NAME,
        name_en=FRONTEND_CATEGORY_NAME,
        icon="fas fa-laptop-code",
        order=1,
    )
    for skill in FRONTEND_SKILLS:
        Skill.objects.create(category=category, **skill)

    set_project_tags(Project, OLD_PROJECT_TAGS)
    Project.objects.filter(title="E-commerce Ibeize").update(
        description=OLD_IBEIZE_DESCRIPTION,
        description_en=OLD_IBEIZE_DESCRIPTION_EN,
    )

    Experience.objects.filter(company="iBeize").update(
        skills=OLD_IBEIZE_SKILLS,
        skills_en=OLD_IBEIZE_SKILLS,
        details=OLD_IBEIZE_DETAILS,
        details_en=OLD_IBEIZE_DETAILS_EN,
    )

    Experience.objects.filter(company="Prisma Informática").update(
        skills=OLD_PRISMA_SKILLS,
        skills_en=OLD_PRISMA_SKILLS_EN,
        details=OLD_PRISMA_DETAILS,
        details_en=OLD_PRISMA_DETAILS_EN,
    )


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0020_three_details_per_experience"),
    ]

    operations = [
        migrations.RunPython(apply_changes, revert_changes),
    ]
