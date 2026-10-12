"""Gera os previews dos cards das coleções (python-projects e data_science_projects).

Lista as pastas de cada repositório pela API pública do GitHub e desenha a
capa: quantidade de projetos em destaque e a árvore de pastas do repositório,
nas cores do site. Rode de novo sempre que adicionar um projeto a uma das
coleções (precisa de internet; usa o Pillow já instalado):

    make previews        (ou: python scripts/collection_previews.py)
"""

import json
import sys
import urllib.request
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

GITHUB_USER = "davioliveiraes"
OUT_DIR = Path(__file__).resolve().parent.parent / "static" / "images" / "projects"

# repo -> (arquivo de saída, subtítulo, motivo desenhado no canto)
COLLECTIONS = {
    "python-projects": (
        "python-projects.webp",
        "APIs, integrações e automações em Python",
        "code",
    ),
    "data_science_projects": (
        "data-science-projects.webp",
        "Análises, estatística e machine learning",
        "chart",
    ),
}

# Desenha em 2x e reduz no fim: texto mais nítido no tamanho final (920x460)
S = 2
W, H = 920 * S, 460 * S

# Tokens do tema escuro (static/css/style.css)
TINT = (33, 52, 63)  # --pf-tint, fundo das capas dos cards
DOT = (55, 68, 81)  # --pf-rule a 40% sobre o tint (malha de pontos)
BG = (22, 24, 38)  # --pf-bg
BORDER = (56, 58, 70)  # --pf-border sobre o bg
TEXT = (233, 233, 237)  # --pf-text
MUTED = (147, 151, 171)  # --pf-muted
RULE = (89, 93, 108)  # --pf-rule
ACCENT = (54, 117, 136)  # --pf-accent
ACCENT_LIGHT = (111, 176, 196)  # accent clareado para contraste sobre o tint

FONT_CANDIDATES = {
    "sans": ["segoeui.ttf", "DejaVuSans.ttf", "Arial.ttf"],
    "sans_bold": ["seguisb.ttf", "DejaVuSans-Bold.ttf", "Arial Bold.ttf"],
    "mono": ["consola.ttf", "DejaVuSansMono.ttf", "Menlo.ttc"],
}
FONT_DIRS = [
    Path("C:/Windows/Fonts"),
    Path("/usr/share/fonts/truetype/dejavu"),
    Path("/Library/Fonts"),
    Path("/System/Library/Fonts"),
]


def font(kind, size):
    for name in FONT_CANDIDATES[kind]:
        for folder in FONT_DIRS:
            if (folder / name).exists():
                return ImageFont.truetype(str(folder / name), size * S)
    sys.exit(f"Fonte não encontrada para '{kind}': instale {FONT_CANDIDATES[kind]}")


def list_projects(repo):
    """Pastas na raiz do repositório = projetos da coleção."""
    request = urllib.request.Request(
        f"https://api.github.com/repos/{GITHUB_USER}/{repo}/contents",
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "davioliveira.tech-previews",
        },
    )
    with urllib.request.urlopen(request, timeout=10) as response:
        entries = json.load(response)
    return sorted(e["name"] for e in entries if e["type"] == "dir")


def spaced_text(draw, xy, text, fnt, fill, spacing):
    """Texto com letter-spacing, como os kickers do site."""
    x, y = xy
    for char in text:
        draw.text((x, y), char, font=fnt, fill=fill)
        x += draw.textlength(char, font=fnt) + spacing * S


def draw_dots(draw):
    step = 16 * S
    for x in range(step // 2, W, step):
        for y in range(step // 2, H, step):
            draw.ellipse((x - S, y - S, x + S, y + S), fill=DOT)


def draw_motif(draw, kind, x, y):
    """Ícone abstrato no canto: linhas de código ou gráfico de barras."""
    if kind == "code":
        rows = [(0, 120, ACCENT_LIGHT), (24, 150, RULE), (24, 96, RULE), (0, 64, RULE)]
        for i, (indent, width, color) in enumerate(rows):
            top = y + i * 18 * S
            draw.rounded_rectangle(
                (x + indent * S, top, x + (indent + width) * S, top + 8 * S),
                radius=4 * S,
                fill=color,
            )
    else:
        heights = [26, 42, 34, 58, 48, 70]
        base = y + 70 * S
        for i, h in enumerate(heights):
            left = x + i * 22 * S
            color = ACCENT_LIGHT if i == len(heights) - 1 else RULE
            draw.rounded_rectangle(
                (left, base - h * S, left + 14 * S, base), radius=3 * S, fill=color
            )


def draw_tree(draw, repo, projects, box):
    """Janela com a árvore de pastas; se não couber, a última linha resume."""
    x0, y0, x1, y1 = box
    draw.rounded_rectangle(box, radius=10 * S, fill=BG, outline=BORDER, width=S)

    # Barra de título
    bar = 34 * S
    draw.line((x0, y0 + bar, x1, y0 + bar), fill=BORDER, width=S)
    for i in range(3):
        cx, cy = x0 + (18 + i * 14) * S, y0 + bar // 2
        draw.ellipse((cx - 4 * S, cy - 4 * S, cx + 4 * S, cy + 4 * S), fill=RULE)
    draw.text(
        (x0 + 70 * S, y0 + 10 * S),
        f"{GITHUB_USER}/{repo}",
        font=font("mono", 13),
        fill=MUTED,
    )

    mono = font("mono", 14)
    line_h = 20 * S
    x, y = x0 + 18 * S, y0 + bar + 14 * S
    draw.text((x, y), f"{repo}/", font=font("mono", 14), fill=ACCENT_LIGHT)
    y += line_h

    rows_fit = (y1 - 12 * S - y) // line_h
    shown = projects
    if len(projects) > rows_fit:
        shown = projects[: rows_fit - 1]

    max_w = x1 - 18 * S - x
    for i, name in enumerate(shown):
        last = i == len(shown) - 1 and len(shown) == len(projects)
        branch = "└─ " if last else "├─ "
        draw.text((x, y), branch, font=mono, fill=RULE)
        nx = x + draw.textlength(branch, font=mono)
        label = name
        while draw.textlength(label + "/", font=mono) > max_w - (nx - x):
            label = label[:-2] + "…"
        draw.text((nx, y), label, font=mono, fill=TEXT)
        draw.text(
            (nx + draw.textlength(label, font=mono), y), "/", font=mono, fill=ACCENT
        )
        y += line_h

    if len(shown) < len(projects):
        rest = len(projects) - len(shown)
        draw.text((x, y), "└─ ", font=mono, fill=RULE)
        draw.text(
            (x + draw.textlength("└─ ", font=mono), y),
            f"+{rest} projetos",
            font=mono,
            fill=MUTED,
        )


def render(repo, filename, subtitle, motif):
    projects = list_projects(repo)
    image = Image.new("RGB", (W, H), TINT)
    draw = ImageDraw.Draw(image)
    draw_dots(draw)

    # Coluna da esquerda: kicker, contagem e subtítulo
    left = 48 * S
    spaced_text(
        draw,
        (left, 60 * S),
        "COLEÇÃO NO GITHUB",
        font("sans_bold", 13),
        ACCENT_LIGHT,
        2,
    )
    count_font = font("sans_bold", 104)
    draw.text((left, 76 * S), str(len(projects)), font=count_font, fill=TEXT)
    # "projetos" logo abaixo do desenho do número (a fonte tem muito respiro)
    count_bottom = draw.textbbox((left, 76 * S), str(len(projects)), font=count_font)[3]
    label_y = count_bottom + 14 * S
    draw.text((left + 4 * S, label_y), "projetos", font=font("sans", 30), fill=TEXT)

    words, lines, line = subtitle.split(), [], ""
    sub_font = font("sans", 18)
    for word in words:
        candidate = f"{line} {word}".strip()
        if draw.textlength(candidate, font=sub_font) > 350 * S:
            lines.append(line)
            line = word
        else:
            line = candidate
    lines.append(line)
    for i, text in enumerate(lines):
        draw.text(
            (left + 4 * S, label_y + (52 + i * 26) * S), text, font=sub_font, fill=MUTED
        )

    draw_motif(draw, motif, left + 4 * S, 350 * S)
    draw_tree(draw, repo, projects, (420 * S, 32 * S, 880 * S, 428 * S))

    final = image.resize((W // S, H // S), Image.LANCZOS)
    path = OUT_DIR / filename
    final.save(path, "WEBP", quality=90, method=6)
    print(f"{path.relative_to(OUT_DIR.parent.parent.parent)}: {len(projects)} projetos")


def main():
    for repo, (filename, subtitle, motif) in COLLECTIONS.items():
        render(repo, filename, subtitle, motif)


if __name__ == "__main__":
    main()
