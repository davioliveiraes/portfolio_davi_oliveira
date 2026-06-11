"""Preenche traduções EN pendentes no django.po (uso único, rodar da raiz)."""

import polib

TRANSLATIONS = {
    # Meta tags / Open Graph
    "Davi Oliveira — Engenheiro de Software backend com expertise em Python, "
    "Django e FastAPI. Clean Architecture, testes, automações e IA aplicada.": (
        "Davi Oliveira — Backend Software Engineer with expertise in Python, "
        "Django and FastAPI. Clean Architecture, testing, automation and applied AI."
    ),
    "Backend com Python, Django e FastAPI. Clean Architecture, testes, "
    "automações e IA aplicada.": (
        "Backend with Python, Django and FastAPI. Clean Architecture, "
        "testing, automation and applied AI."
    ),
    "Davi Oliveira — Engenheiro de Software": "Davi Oliveira — Software Engineer",
    # Header
    "Alternar tema": "Toggle theme",
    # Home / hero
    "Engenheiro de Software Backend|Python · Django · FastAPI|Clean "
    "Architecture &amp; Testes|Automações, Dados &amp; IA": (
        "Backend Software Engineer|Python · Django · FastAPI|Clean "
        "Architecture &amp; Testing|Automation, Data &amp; AI"
    ),
    "Construo APIs, automações e soluções com IA em Python — com código "
    "limpo, testes e arquitetura preparada para crescer. Atualmente "
    "explorando Go (Golang).": (
        "I build APIs, automations and AI-powered solutions in Python — with "
        "clean code, testing and an architecture ready to grow. Currently "
        "exploring Go (Golang)."
    ),
    # Projetos
    "Código": "Code",
    "Ver site": "View site",
    # Experiências (iBeize)
    "Customização do storefront via CSS/HTML/JS/GoTemplate avançado e "
    "integração com ERP GestãoClick": (
        "Storefront customization via advanced CSS/HTML/JS/GoTemplate and "
        "integration with GestãoClick ERP"
    ),
    "Desenvolvimento do Ibeize Ecommerce Control — sistema interno fullstack "
    "(Django Ninja + React + Docker) para gestão de catálogo e finanças": (
        "Development of Ibeize Ecommerce Control — internal fullstack system "
        "(Django Ninja + React + Docker) for catalog and finance management"
    ),
    "NuvemShop, GestãoClick, CSS, HTML, JavaScript, GoTemplate, Django Ninja, "
    "React, Docker, KPIs, ROI, DNS, Melhor Envio": (
        "NuvemShop, GestãoClick, CSS, HTML, JavaScript, GoTemplate, Django "
        "Ninja, React, Docker, KPIs, ROI, DNS, Melhor Envio"
    ),
    # Certificações
    "Imersão Build & Automate — Desenvolvimento e Automação com IA": (
        "Build & Automate Immersion — Development and Automation with AI"
    ),
    "Logic Master — Lógica de Programação e Algoritmos com Python": (
        "Logic Master — Programming Logic and Algorithms with Python"
    ),
    "Autenticação JWT e Segurança": "JWT Authentication and Security",
    # Sobre — parágrafo 1
    "Minha trajetória na tecnologia começou com a formação técnica em "
    "Informática, onde tive meus primeiros contatos com lógica de programação "
    "e desenvolvimento de sistemas. A curiosidade de entender como a "
    "tecnologia funciona por trás das telas despertou o desejo de me "
    "aprofundar na área, o que me levou à graduação em Engenharia de "
    "Software. Foi nesse caminho que construí uma base sólida e desenvolvi "
    "uma visão mais estruturada sobre como criar soluções que realmente façam "
    "sentido para as pessoas e para os negócios.": (
        "My journey in technology began with a technical degree in "
        "Informatics, where I had my first contact with programming logic and "
        "systems development. The curiosity to understand how technology "
        "works behind the screens sparked the desire to go deeper into the "
        "field, which led me to a bachelor's degree in Software Engineering. "
        "It was along this path that I built a solid foundation and developed "
        "a more structured vision of how to create solutions that truly make "
        "sense for people and businesses."
    ),
    # Sobre — parágrafo 2
    "Hoje, atuo com foco no desenvolvimento backend em Python, criando APIs e "
    "aplicações utilizando frameworks como FastAPI e Django. Gosto de "
    "desenvolver soluções organizadas, integrando serviços, trabalhando com "
    "PostgreSQL e aplicando boas práticas que garantam código limpo, "
    "manutenção facilitada e evolução contínua dos sistemas. Mais do que "
    "fazer o software funcionar, busco construir aplicações confiáveis e "
    "preparadas para crescer.": (
        "Today, I focus on backend development in Python, building APIs and "
        "applications with frameworks such as FastAPI and Django. I enjoy "
        "creating well-organized solutions, integrating services, working "
        "with PostgreSQL and applying best practices that ensure clean code, "
        "easy maintenance and continuous system evolution. More than making "
        "software work, I aim to build reliable applications that are ready "
        "to grow."
    ),
    # Sobre — parágrafo 3
    "Ao longo dessa jornada, percebi que backend não se resume apenas à "
    "lógica de negócio. Por isso, também aprofundei meus conhecimentos em "
    "análise de dados com Python e em automação de processos, transformando "
    "tarefas repetitivas em fluxos mais eficientes e utilizando dados para "
    "apoiar decisões e gerar valor. Essa visão mais ampla me permite enxergar "
    "a tecnologia como uma ferramenta para resolver problemas reais de forma "
    "prática e inteligente.": (
        "Along this journey, I realized that backend is not just about "
        "business logic. That is why I also deepened my knowledge of data "
        "analysis with Python and process automation, turning repetitive "
        "tasks into more efficient workflows and using data to support "
        "decisions and generate value. This broader perspective allows me to "
        "see technology as a tool to solve real problems in a practical and "
        "intelligent way."
    ),
    # Sobre — parágrafo 4
    "Atualmente, atuo como Analista de E-commerce na iBeize, onde aplico "
    "desenvolvimento, automação e análise de dados em uma operação real — "
    "incluindo a construção de um sistema interno fullstack. Sigo expandindo "
    "meus conhecimentos em Go (Golang) e Inteligência Artificial aplicada, "
    "sempre movido pela vontade de aprender e evoluir, e estou em busca de "
    "novas oportunidades na área de desenvolvimento para contribuir com "
    "soluções bem estruturadas e crescer ao lado de equipes que valorizam "
    "qualidade, colaboração e inovação. Meu objetivo é transformar "
    "tecnologia, dados e boas ideias em impacto real.": (
        "I currently work as an E-commerce Analyst at iBeize, where I apply "
        "development, automation and data analysis to a real operation — "
        "including building an internal fullstack system. I keep expanding my "
        "knowledge of Go (Golang) and applied Artificial Intelligence, always "
        "driven by the desire to learn and evolve, and I am looking for new "
        "opportunities in software development to contribute with "
        "well-structured solutions and grow alongside teams that value "
        "quality, collaboration and innovation. My goal is to turn "
        "technology, data and good ideas into real impact."
    ),
}


def main():
    po = polib.pofile("locale/en/LC_MESSAGES/django.po")
    applied = 0
    for entry in po:
        if entry.msgid in TRANSLATIONS:
            entry.msgstr = TRANSLATIONS[entry.msgid]
            if "fuzzy" in entry.flags:
                entry.flags.remove("fuzzy")
            entry.previous_msgid = None
            applied += 1
    po.save()
    print(f"{applied} traduções aplicadas de {len(TRANSLATIONS)} previstas")

    remaining = [e for e in po if not e.msgstr and not e.obsolete]
    fuzzy = [e for e in po if "fuzzy" in e.flags]
    print(f"Pendentes: {len(remaining)} | Fuzzy: {len(fuzzy)}")
    for e in remaining + fuzzy:
        print(" -", e.msgid[:80])


if __name__ == "__main__":
    main()
