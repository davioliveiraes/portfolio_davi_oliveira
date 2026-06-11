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
// TYPEWRITER (hero)
// ============================================
const typewriter = document.getElementById('typewriter');

if (typewriter) {
    const phrases = typewriter.dataset.phrases.split('|');
    const textEl = document.getElementById('typewriterText');

    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
        textEl.textContent = phrases[0];
    } else {
        let phraseIndex = 0;
        let charIndex = 0;
        let deleting = false;

        (function tick() {
            const phrase = phrases[phraseIndex];
            charIndex += deleting ? -1 : 1;
            textEl.textContent = phrase.slice(0, charIndex);

            let delay = deleting ? 40 : 85;
            if (!deleting && charIndex === phrase.length) {
                deleting = true;
                delay = 2200; // pausa com a frase completa
            } else if (deleting && charIndex === 0) {
                deleting = false;
                phraseIndex = (phraseIndex + 1) % phrases.length;
                delay = 400;
            }
            setTimeout(tick, delay);
        })();
    }
}

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
        if (cmd.external) {
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
