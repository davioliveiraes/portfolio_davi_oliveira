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
// ANIMAÇÃO DE ENTRADA NO SCROLL
// ============================================
const revealSelector = '.skill-card, .project-card, .timeline-card, .formation-card, .info-item, .section-header';

if ('IntersectionObserver' in window && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                revealObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

    document.querySelectorAll(revealSelector).forEach(el => {
        const siblingIndex = Array.from(el.parentElement.children).indexOf(el);
        el.style.transitionDelay = `${(siblingIndex % 4) * 70}ms`;
        el.classList.add('reveal');
        revealObserver.observe(el);
    });
}

// ============================================
// FILTRO DE PROJETOS POR TECNOLOGIA
// ============================================
const projectFilters = document.getElementById('projectFilters');

if (projectFilters) {
    const filterButtons = projectFilters.querySelectorAll('.filter-btn');
    const projectCards = document.querySelectorAll('.project-card');
    const emptyMessage = document.getElementById('projectsEmpty');

    filterButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            filterButtons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const filter = btn.dataset.filter;
            let visible = 0;
            projectCards.forEach(card => {
                const show = filter === 'all' || card.dataset.category === filter;
                card.classList.toggle('filtered-out', !show);
                if (show) visible++;
            });
            if (emptyMessage) emptyMessage.hidden = visible > 0;
        });
    });
}

// ============================================
// MENU MOBILE
// ============================================
const menuToggle = document.querySelector('.menu-toggle');
const navLinks = document.querySelector('.nav-links');

menuToggle.addEventListener('click', () => {
    menuToggle.classList.toggle('active');
    navLinks.classList.toggle('open');
});

navLinks.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
        menuToggle.classList.remove('active');
        navLinks.classList.remove('open');
    });
});

document.addEventListener('click', (e) => {
    if (!menuToggle.contains(e.target) && !navLinks.contains(e.target)) {
        menuToggle.classList.remove('active');
        navLinks.classList.remove('open');
    }
});

// ============================================
// COMMAND PALETTE
// ============================================
const palette = {
    overlay: document.getElementById('paletteOverlay'),
    input: document.getElementById('paletteInput'),
    results: document.getElementById('paletteResults'),
    selectedIndex: -1,

    commands: [
        { label: 'Home', desc: 'Página inicial', icon: 'fas fa-home', url: '/' },
        { label: 'Sobre', desc: 'Sobre mim', icon: 'fas fa-user', url: '/sobre/' },
        { label: 'Competências', desc: 'Competências técnicas', icon: 'fas fa-code', url: '/competencias/' },
        { label: 'Projetos', desc: 'Meus projetos', icon: 'fas fa-folder-open', url: '/projetos/' },
        { label: 'Experiências', desc: 'Experiências profissionais', icon: 'fas fa-briefcase', url: '/experiencias/' },
        { label: 'Formação', desc: 'Formação acadêmica', icon: 'fas fa-graduation-cap', url: '/formacao/' },
        { label: 'Contato', desc: 'Entre em contato', icon: 'fas fa-envelope', url: '/contato/' },
        { label: 'GitHub', desc: 'Abrir perfil no GitHub', icon: 'fab fa-github', url: 'https://github.com/davioliveiraes', external: true },
        { label: 'LinkedIn', desc: 'Abrir perfil no LinkedIn', icon: 'fab fa-linkedin-in', url: 'https://www.linkedin.com/in/davioliveiraes/', external: true },
    ],

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
        return this.commands.filter(cmd =>
            cmd.label.toLowerCase().includes(q) ||
            cmd.desc.toLowerCase().includes(q)
        );
    },

    render(items) {
        this.results.innerHTML = '';
        items.forEach((cmd, i) => {
            const li = document.createElement('li');
            li.className = 'palette-item' + (i === this.selectedIndex ? ' selected' : '');
            li.innerHTML = `
                <div class="palette-icon"><i class="${cmd.icon}"></i></div>
                <div class="palette-label">
                    <span>${cmd.label}</span>
                    <small>${cmd.desc}</small>
                </div>
            `;
            li.addEventListener('click', () => this.navigate(cmd));
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

    navigate(cmd) {
        this.close();
        if (cmd.action) {
            cmd.action();
        } else if (cmd.external) {
            window.open(cmd.url, '_blank', 'noopener');
        } else {
            window.location.href = cmd.url;
        }
    },

    handleKeydown(e) {
        const items = this.results.querySelectorAll('.palette-item');
        const count = items.length;

        if (e.key === 'ArrowDown') {
            e.preventDefault();
            this.selectedIndex = (this.selectedIndex + 1) % count;
            this.updateSelection();
        } else if (e.key === 'ArrowUp') {
            e.preventDefault();
            this.selectedIndex = (this.selectedIndex - 1 + count) % count;
            this.updateSelection();
        } else if (e.key === 'Enter' && this.selectedIndex >= 0) {
            e.preventDefault();
            const filtered = this.filter(this.input.value);
            if (filtered[this.selectedIndex]) {
                this.navigate(filtered[this.selectedIndex]);
            }
        } else if (e.key === 'Escape') {
            this.close();
        }
    }
};

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
    const filtered = palette.filter(palette.input.value);
    palette.render(filtered);
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
    isEN: (document.documentElement.lang || 'pt-br').startsWith('en'),

    t(pt, en) {
        return this.isEN ? en : pt;
    },

    pagePath(path) {
        return this.isEN ? '/en' + path : path;
    },

    open() {
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

        const go = (path) => {
            this.print(this.t('Abrindo', 'Opening') + ' ' + path + '...');
            setTimeout(() => { window.location.href = this.pagePath(path); }, 350);
        };

        const commands = {
            help: () => this.print(this.t(
                'Comandos disponíveis:\n  <span class="term-accent">sobre</span>        quem eu sou\n  <span class="term-accent">projetos</span>     o que eu construí\n  <span class="term-accent">skills</span>       tecnologias que uso\n  <span class="term-accent">experiencia</span>  minha trajetória\n  <span class="term-accent">formacao</span>     estudos e certificações\n  <span class="term-accent">contato</span>      vamos conversar\n  <span class="term-accent">github</span>       meu GitHub\n  <span class="term-accent">linkedin</span>     meu LinkedIn\n  <span class="term-accent">theme</span>        alternar dark/light\n  <span class="term-accent">whoami</span>       ?\n  <span class="term-accent">clear</span>        limpar a tela\n  <span class="term-accent">exit</span>         fechar o terminal',
                'Available commands:\n  <span class="term-accent">about</span>        who I am\n  <span class="term-accent">projects</span>     what I have built\n  <span class="term-accent">skills</span>       technologies I use\n  <span class="term-accent">experience</span>   my journey\n  <span class="term-accent">education</span>    studies and certifications\n  <span class="term-accent">contact</span>      let\'s talk\n  <span class="term-accent">github</span>       my GitHub\n  <span class="term-accent">linkedin</span>     my LinkedIn\n  <span class="term-accent">theme</span>        toggle dark/light\n  <span class="term-accent">whoami</span>       ?\n  <span class="term-accent">clear</span>        clear the screen\n  <span class="term-accent">exit</span>         close the terminal'
            )),
            sobre: () => go('/sobre/'),
            about: () => go('/sobre/'),
            projetos: () => go('/projetos/'),
            projects: () => go('/projetos/'),
            skills: () => go('/competencias/'),
            competencias: () => go('/competencias/'),
            experiencia: () => go('/experiencias/'),
            experiencias: () => go('/experiencias/'),
            experience: () => go('/experiencias/'),
            formacao: () => go('/formacao/'),
            education: () => go('/formacao/'),
            contato: () => go('/contato/'),
            contact: () => go('/contato/'),
            github: () => { window.open('https://github.com/davioliveiraes', '_blank', 'noopener'); this.print('GitHub ↗'); },
            linkedin: () => { window.open('https://www.linkedin.com/in/davioliveiraes/', '_blank', 'noopener'); this.print('LinkedIn ↗'); },
            theme: () => {
                document.getElementById('themeToggle').click();
                this.print(this.t('Tema alternado. 🎨', 'Theme toggled. 🎨'));
            },
            whoami: () => this.print(this.t(
                'Um(a) visitante curioso(a) — e isso já diz muito sobre você. 👀\nCuriosidade é requisito da vaga, aliás.',
                'A curious visitor — and that already says a lot about you. 👀\nCuriosity happens to be a job requirement.'
            )),
            ls: () => this.print('sobre/  projetos/  competencias/  experiencias/  formacao/  contato/'),
            pwd: () => this.print('/home/davi/portfolio'),
            date: () => this.print(new Date().toLocaleString(this.isEN ? 'en-US' : 'pt-BR')),
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
                `comando não encontrado: ${cmd}. Tente <span class="term-accent">help</span>.`,
                `command not found: ${cmd}. Try <span class="term-accent">help</span>.`
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
        label: 'Terminal',
        desc: terminal.t('Modo terminal (easter egg)', 'Terminal mode (easter egg)'),
        icon: 'fas fa-terminal',
        action: () => terminal.open(),
    });

    // Dica para quem abre o DevTools
    console.log('%c$ davi@portfolio:~  —  ' + terminal.t('aperte Ctrl+` para abrir o terminal secreto', 'press Ctrl+` to open the secret terminal'), 'font-family: monospace; color: #5fb3c9;');
}
