// ============================================
// THEME TOGGLE (dark / light)
// ============================================
const themeToggle = document.getElementById('themeToggle');

themeToggle.addEventListener('click', () => {
    const current = document.documentElement.getAttribute('data-theme');
    const next = current === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
});

// Sincroniza com mudança no sistema operacional (se o usuário não definiu manualmente)
window.matchMedia('(prefers-color-scheme: light)').addEventListener('change', (e) => {
    if (!localStorage.getItem('theme')) {
        document.documentElement.setAttribute('data-theme', e.matches ? 'light' : 'dark');
    }
});

// ============================================
// SCROLL-SPY (link ativo na nav conforme a seção visível)
// ============================================
const navLinks = document.querySelectorAll('#siteNav a[data-section]');
const sections = [];
navLinks.forEach((link) => {
    const el = document.getElementById(link.dataset.section);
    if (el) sections.push(el);
});

if ('IntersectionObserver' in window && sections.length) {
    const spy = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                navLinks.forEach((link) => {
                    link.classList.toggle('active', link.dataset.section === entry.target.id);
                });
            }
        });
    }, { rootMargin: '-45% 0px -50% 0px' });
    sections.forEach((el) => spy.observe(el));
}

// ============================================
// ANIMAÇÃO DE ENTRADA NO SCROLL
// O conteúdo nasce visível; a classe .reveal-in só dispara o enfeite
// de entrada (nunca deixar elemento com opacity: 0 no estado inicial).
// ============================================
if ('IntersectionObserver' in window && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add('reveal-in');
                revealObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.08 });

    document.querySelectorAll('.reveal').forEach((el) => revealObserver.observe(el));
}

// ============================================
// CARROSSEL (experiência, habilidades, projetos e certificações)
// Pagina os itens na horizontal para a seção não crescer conforme o conteúdo aumenta
// ============================================
function initCarousel(root) {
    const viewport = root.querySelector('.carousel-viewport');
    const track = root.querySelector('.carousel-track');
    if (!viewport || !track) return null;

    const controls = root.querySelector('.carousel-controls');
    const dotsBox = root.querySelector('.carousel-dots');
    const countLabel = root.querySelector('.carousel-count');
    const prevBtn = root.querySelector('.carousel-arrow[data-dir="prev"]');
    const nextBtn = root.querySelector('.carousel-arrow[data-dir="next"]');
    const items = Array.from(track.children);

    const visibleItems = () => items.filter((item) => !item.classList.contains('filtered-out'));
    const gapSize = () => parseFloat(getComputedStyle(track).columnGap) || 0;
    const rows = () => Math.max(1, parseInt(getComputedStyle(root).getPropertyValue('--rows'), 10) || 1);
    const maxScroll = () => Math.max(0, viewport.scrollWidth - viewport.clientWidth);

    // Colunas visíveis: derivadas da largura real do item, que o CSS controla por breakpoint
    function perView() {
        const first = visibleItems()[0];
        if (!first) return 1;
        const width = first.getBoundingClientRect().width;
        if (!width) return 1;
        return Math.max(1, Math.round((viewport.clientWidth + gapSize()) / (width + gapSize())));
    }

    const pageCount = () => Math.max(1, Math.ceil(visibleItems().length / (perView() * rows())));

    // Uma página avança colunas inteiras, então a rolagem sempre para na borda de um item
    function step() {
        const first = visibleItems()[0];
        if (!first) return viewport.clientWidth;
        return (first.getBoundingClientRect().width + gapSize()) * perView();
    }

    function currentPage() {
        const pages = pageCount();
        if (pages < 2) return 0;
        if (viewport.scrollLeft >= maxScroll() - 2) return pages - 1;
        return Math.min(pages - 1, Math.round(viewport.scrollLeft / step()));
    }

    function goTo(page) {
        const clamped = Math.min(Math.max(page, 0), pageCount() - 1);
        viewport.scrollTo({ left: Math.min(clamped * step(), maxScroll()), behavior: 'smooth' });
    }

    function render() {
        const pages = pageCount();
        const page = currentPage();

        if (controls) controls.hidden = pages < 2;
        if (countLabel) countLabel.textContent = pages > 1 ? page + 1 + ' / ' + pages : '';
        if (prevBtn) prevBtn.disabled = page === 0;
        if (nextBtn) nextBtn.disabled = page >= pages - 1;

        if (!dotsBox) return;
        if (dotsBox.childElementCount !== pages) {
            const pageWord = ((window.PF || {}).lang || 'pt-br').startsWith('en') ? 'Page ' : 'Página ';
            dotsBox.textContent = '';
            for (let i = 0; i < pages; i++) {
                const dot = document.createElement('button');
                dot.type = 'button';
                dot.className = 'carousel-dot';
                dot.setAttribute('aria-label', pageWord + (i + 1));
                dot.addEventListener('click', () => goTo(i));
                dotsBox.appendChild(dot);
            }
        }
        Array.from(dotsBox.children).forEach((dot, i) => {
            dot.classList.toggle('active', i === page);
        });
    }

    let ticking = false;
    function scheduleRender() {
        if (ticking) return;
        ticking = true;
        requestAnimationFrame(() => {
            ticking = false;
            render();
        });
    }

    viewport.addEventListener('scroll', scheduleRender, { passive: true });
    window.addEventListener('resize', scheduleRender);
    window.addEventListener('load', render);

    if (prevBtn) prevBtn.addEventListener('click', () => goTo(currentPage() - 1));
    if (nextBtn) nextBtn.addEventListener('click', () => goTo(currentPage() + 1));

    viewport.addEventListener('keydown', (event) => {
        if (event.key === 'ArrowRight') {
            event.preventDefault();
            goTo(currentPage() + 1);
        } else if (event.key === 'ArrowLeft') {
            event.preventDefault();
            goTo(currentPage() - 1);
        }
    });

    render();

    return {
        render: render,
        // Usado pelo filtro: volta ao começo da lista e recalcula as páginas
        reset: function () {
            viewport.scrollTo({ left: 0, behavior: 'auto' });
            render();
        },
    };
}

const carousels = new Map();
document.querySelectorAll('.carousel').forEach((root) => {
    const api = initCarousel(root);
    if (api) carousels.set(root.id, api);
});

// ============================================
// FILTRO DE PROJETOS POR CATEGORIA
// ============================================
const projectFilters = document.getElementById('projectFilters');

if (projectFilters) {
    const filterButtons = projectFilters.querySelectorAll('.filter-pill');
    const projectCards = document.querySelectorAll('.project-card');
    const emptyMessage = document.getElementById('projectsEmpty');

    filterButtons.forEach((btn) => {
        btn.addEventListener('click', () => {
            filterButtons.forEach((b) => b.classList.remove('active'));
            btn.classList.add('active');

            const filter = btn.dataset.filter;
            let visible = 0;
            projectCards.forEach((card) => {
                const show = filter === 'all' || card.dataset.category === filter;
                card.classList.toggle('filtered-out', !show);
                if (show) visible++;
            });
            if (emptyMessage) emptyMessage.hidden = visible > 0;

            const carousel = carousels.get('projectsCarousel');
            if (carousel) carousel.reset();
        });
    });
}

// ============================================
// COMMAND PALETTE
// ============================================
const PF = window.PF || { lang: 'pt-br', i18n: {} };
const isEN = (PF.lang || 'pt-br').startsWith('en');

function scrollToSection(id) {
    const el = document.getElementById(id);
    if (el) el.scrollIntoView({ behavior: 'smooth' });
}

const palette = {
    overlay: document.getElementById('paletteOverlay'),
    input: document.getElementById('paletteInput'),
    results: document.getElementById('paletteResults'),
    selectedIndex: -1,

    // Seções vêm da própria nav (já traduzidas pelo template)
    commands: Array.from(navLinks).map((link) => ({
        label: link.textContent.trim(),
        hint: PF.i18n.section || 'Seção',
        action: () => scrollToSection(link.dataset.section),
    })),

    open() {
        this.overlay.classList.add('open');
        this.input.value = '';
        this.selectedIndex = -1;
        this.render(this.commands);
        setTimeout(() => this.input.focus(), 50);
    },

    close() {
        this.overlay.classList.remove('open');
        this.input.blur();
    },

    toggle() {
        this.overlay.classList.contains('open') ? this.close() : this.open();
    },

    filter(query) {
        if (!query) return this.commands;
        const q = query.toLowerCase();
        return this.commands.filter((cmd) => cmd.label.toLowerCase().includes(q));
    },

    render(items) {
        this.results.innerHTML = '';
        items.forEach((cmd, i) => {
            const li = document.createElement('li');
            li.className = 'palette-item' + (i === this.selectedIndex ? ' selected' : '');
            const label = document.createElement('span');
            label.textContent = cmd.dynamicLabel ? cmd.dynamicLabel() : cmd.label;
            const hint = document.createElement('small');
            hint.textContent = cmd.hint;
            li.append(label, hint);
            li.addEventListener('click', () => this.run(cmd));
            li.addEventListener('mouseenter', () => {
                this.selectedIndex = i;
                this.updateSelection();
            });
            this.results.appendChild(li);
        });
    },

    updateSelection() {
        const items = this.results.querySelectorAll('.palette-item');
        items.forEach((item, i) => {
            item.classList.toggle('selected', i === this.selectedIndex);
        });
        const selected = items[this.selectedIndex];
        if (selected) selected.scrollIntoView({ block: 'nearest' });
    },

    run(cmd) {
        this.close();
        cmd.action();
    },

    handleKeydown(e) {
        const filtered = this.filter(this.input.value);
        const count = filtered.length;

        if (e.key === 'ArrowDown') {
            e.preventDefault();
            this.selectedIndex = (this.selectedIndex + 1) % count;
            this.updateSelection();
        } else if (e.key === 'ArrowUp') {
            e.preventDefault();
            this.selectedIndex = (this.selectedIndex - 1 + count) % count;
            this.updateSelection();
        } else if (e.key === 'Enter') {
            e.preventDefault();
            const cmd = filtered[this.selectedIndex] || filtered[0];
            if (cmd) this.run(cmd);
        } else if (e.key === 'Escape') {
            this.close();
        }
    }
};

// Ações além das seções
palette.commands.push(
    {
        label: PF.i18n.themeDark || 'Tema escuro',
        dynamicLabel: () => (document.documentElement.getAttribute('data-theme') === 'dark'
            ? (PF.i18n.themeLight || 'Tema claro')
            : (PF.i18n.themeDark || 'Tema escuro')),
        hint: PF.i18n.action || 'Ação',
        action: () => themeToggle.click(),
    },
    {
        label: PF.i18n.switchLang || 'Switch to English',
        hint: PF.i18n.action || 'Ação',
        action: () => document.getElementById('langForm').submit(),
    },
    {
        label: PF.i18n.cv || 'Currículo',
        hint: PF.i18n.download || 'Download',
        action: () => document.getElementById('cvButton').click(),
    },
    {
        label: 'GitHub',
        hint: PF.i18n.link || 'Link',
        action: () => window.open('https://github.com/davioliveiraes', '_blank', 'noopener'),
    },
    {
        label: 'LinkedIn',
        hint: PF.i18n.link || 'Link',
        action: () => window.open('https://www.linkedin.com/in/davioliveiraes/', '_blank', 'noopener'),
    }
);

// Ctrl+K / Cmd+K para abrir
document.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        palette.toggle();
    }
    if (e.key === 'Escape' && palette.overlay.classList.contains('open')) {
        palette.close();
    }
});

// Filtrar ao digitar
palette.input.addEventListener('input', () => {
    palette.selectedIndex = 0;
    palette.render(palette.filter(palette.input.value));
});

// Navegação com teclado dentro da palette
palette.input.addEventListener('keydown', (e) => palette.handleKeydown(e));

// Botão trigger no header
document.getElementById('paletteTrigger').addEventListener('click', () => palette.open());

// Fechar ao clicar no overlay
palette.overlay.addEventListener('click', (e) => {
    if (e.target === palette.overlay) palette.close();
});

// ============================================
// TERMINAL (easter egg) — Ctrl+` ou via palette
// ============================================
const terminal = {
    overlay: document.getElementById('terminalOverlay'),
    output: document.getElementById('terminalOutput'),
    input: document.getElementById('terminalInput'),
    history: [],
    historyIndex: -1,
    booted: false,

    t(pt, en) {
        return isEN ? en : pt;
    },

    open() {
        palette.close();
        this.overlay.classList.add('open');
        if (!this.booted) {
            this.booted = true;
            this.print(this.t(
                'Bem-vindo ao portfólio de <span class="term-accent">Davi Oliveira</span>! 🎉\nVocê encontrou o terminal secreto. Digite <span class="term-accent">help</span> para ver os comandos.',
                "Welcome to <span class=\"term-accent\">Davi Oliveira</span>'s portfolio! 🎉\nYou found the secret terminal. Type <span class=\"term-accent\">help</span> to see the commands."
            ));
        }
        setTimeout(() => this.input.focus(), 50);
    },

    close() {
        this.overlay.classList.remove('open');
        this.input.blur();
    },

    print(html, cssClass = '') {
        const line = document.createElement('div');
        line.className = 'term-line' + (cssClass ? ' ' + cssClass : '');
        line.innerHTML = html;
        this.output.appendChild(line);
        this.output.parentElement.scrollTop = this.output.parentElement.scrollHeight;
    },

    run(raw) {
        const cmd = raw.trim().toLowerCase();
        this.print(`<span class="term-accent">davi@portfolio:~$</span> <span class="term-cmd">${raw.replace(/</g, '&lt;')}</span>`);
        if (!cmd) return;

        this.history.push(raw);
        this.historyIndex = this.history.length;

        const go = (section) => {
            this.print(this.t('Indo para', 'Going to') + ' #' + section + '...');
            this.close();
            scrollToSection(section);
        };

        const commands = {
            help: () => this.print(this.t(
                'Comandos disponíveis:\n  <span class="term-accent">whoami</span>       quem eu sou\n  <span class="term-accent">projetos</span>     o que eu construí\n  <span class="term-accent">skills</span>       tecnologias que uso\n  <span class="term-accent">experiencia</span>  minha trajetória\n  <span class="term-accent">formacao</span>     estudos e certificações\n  <span class="term-accent">contato</span>      vamos conversar\n  <span class="term-accent">social</span>       minhas redes\n  <span class="term-accent">github</span>       meu GitHub\n  <span class="term-accent">linkedin</span>     meu LinkedIn\n  <span class="term-accent">theme</span>        alternar dark/light\n  <span class="term-accent">clear</span>        limpar a tela\n  <span class="term-accent">exit</span>         fechar o terminal',
                'Available commands:\n  <span class="term-accent">whoami</span>       who I am\n  <span class="term-accent">projects</span>     what I have built\n  <span class="term-accent">skills</span>       technologies I use\n  <span class="term-accent">experience</span>   my journey\n  <span class="term-accent">education</span>    studies and certifications\n  <span class="term-accent">contact</span>      let\'s talk\n  <span class="term-accent">social</span>       my networks\n  <span class="term-accent">github</span>       my GitHub\n  <span class="term-accent">linkedin</span>     my LinkedIn\n  <span class="term-accent">theme</span>        toggle dark/light\n  <span class="term-accent">clear</span>        clear the screen\n  <span class="term-accent">exit</span>         close the terminal'
            )),
            whoami: () => this.print(this.t(
                'Davi Oliveira — engenheiro de software. Python, Django, FastAPI, TypeScript, IA aplicada.',
                'Davi Oliveira — software engineer. Python, Django, FastAPI, TypeScript, applied AI.'
            )),
            projetos: () => go('projetos'),
            projects: () => go('projetos'),
            skills: () => go('habilidades'),
            habilidades: () => go('habilidades'),
            experiencia: () => go('experiencia'),
            experiencias: () => go('experiencia'),
            experience: () => go('experiencia'),
            formacao: () => go('formacao'),
            education: () => go('formacao'),
            contato: () => go('contatos'),
            contact: () => go('contatos'),
            social: () => this.print('github.com/davioliveiraes · linkedin.com/in/davioliveiraes · instagram.com/davioliveiraes'),
            github: () => { window.open('https://github.com/davioliveiraes', '_blank', 'noopener'); this.print('GitHub ↗'); },
            linkedin: () => { window.open('https://www.linkedin.com/in/davioliveiraes/', '_blank', 'noopener'); this.print('LinkedIn ↗'); },
            theme: () => {
                themeToggle.click();
                this.print(this.t('Tema alternado. 🎨', 'Theme toggled. 🎨'));
            },
            ls: () => this.print('inicio/  experiencia/  habilidades/  projetos/  formacao/  contatos/'),
            pwd: () => this.print('/home/davi/portfolio'),
            date: () => this.print(new Date().toLocaleString(isEN ? 'en-US' : 'pt-BR')),
            sudo: () => this.print(this.t(
                'davi não está no arquivo sudoers. Este incidente será reportado. 😄',
                'davi is not in the sudoers file. This incident will be reported. 😄'
            ), 'term-error'),
            clear: () => { this.output.innerHTML = ''; },
            exit: () => this.close(),
        };

        if (commands[cmd]) {
            commands[cmd]();
        } else {
            this.print(this.t(
                `comando não encontrado: ${cmd} — tente <span class="term-accent">help</span>`,
                `command not found: ${cmd} — try <span class="term-accent">help</span>`
            ), 'term-error');
        }
    }
};

if (terminal.overlay) {
    // Atalho Ctrl+` (crase)
    document.addEventListener('keydown', (e) => {
        if (e.ctrlKey && (e.key === '`' || e.key === "'")) {
            e.preventDefault();
            terminal.overlay.classList.contains('open') ? terminal.close() : terminal.open();
        }
        if (e.key === 'Escape' && terminal.overlay.classList.contains('open')) {
            terminal.close();
        }
    });

    terminal.input.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
            terminal.run(terminal.input.value);
            terminal.input.value = '';
        } else if (e.key === 'ArrowUp') {
            e.preventDefault();
            if (terminal.historyIndex > 0) {
                terminal.historyIndex--;
                terminal.input.value = terminal.history[terminal.historyIndex];
            }
        } else if (e.key === 'ArrowDown') {
            e.preventDefault();
            if (terminal.historyIndex < terminal.history.length - 1) {
                terminal.historyIndex++;
                terminal.input.value = terminal.history[terminal.historyIndex];
            } else {
                terminal.historyIndex = terminal.history.length;
                terminal.input.value = '';
            }
        }
    });

    document.getElementById('terminalClose').addEventListener('click', () => terminal.close());
    terminal.overlay.addEventListener('click', (e) => {
        if (e.target === terminal.overlay) terminal.close();
    });
    document.getElementById('terminalBody').addEventListener('click', () => terminal.input.focus());

    // Entrada pela Command Palette
    palette.commands.push({
        label: PF.i18n.terminal || 'Terminal',
        hint: 'Ctrl+`',
        action: () => terminal.open(),
    });

    // Dica para quem abre o DevTools
    console.log('%c$ davi@portfolio:~  —  ' + terminal.t('aperte Ctrl+` para abrir o terminal secreto', 'press Ctrl+` to open the secret terminal'), 'font-family: monospace; color: #8fd6a0;');
}
