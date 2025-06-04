<h1 align="center">Portfolio Digital - Davi Oliveira</h1>

<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django"/>
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript"/>
  <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL"/>
</div>

<div align="center">
  <h3>🚀 Uma aplicação web moderna e responsiva para apresentar meu portfólio profissional</h3>
  
  <p>
    <a href="#-sobre-o-projeto">Sobre</a> •
    <a href="#-tecnologias">Tecnologias</a> •
    <a href="#-funcionalidades">Funcionalidades</a> •
    <a href="#-deploy">Deploy</a> 
  </p>

  <a href="https://portfolio-davi-oliveira.onrender.com/" target="_blank">
    <img src="https://img.shields.io/badge/🌐%20Ver%20Portfolio%20Online-4CAF50?style=for-the-badge&logoColor=white" alt="Ver Portfolio"/>
  </a>
</div>

---

## 📋 Sobre o Projeto

Este é meu portfólio digital desenvolvido com **Django**, uma aplicação web completa que apresenta minha trajetória profissional, habilidades técnicas e projetos realizados. O sistema conta com interface administrativa para gerenciamento de conteúdo e design responsivo para uma experiência otimizada em todos os dispositivos.

### ✨ Principais Características

- 🎯 **Interface Moderna**: Design clean e responsivo
- 🔧 **Painel Administrativo**: Gerenciamento completo via Django Admin
- 📱 **Responsivo**: Funciona perfeitamente em desktop, tablet e mobile
- 🚀 **Performance Otimizada**: Carregamento rápido e eficiente
- 🔒 **Seguro**: Implementação de boas práticas de segurança do Django

---

## 🛠️ Tecnologias

### **Backend**
- ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) **Python 3.x**
- ![Django](https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white) **Django 5.1.7**

### **Frontend**
- ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white) **HTML5**
- ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white) **CSS3**
- ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black) **JavaScript ES6+**

### **Banco de Dados**
- ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=flat&logo=postgresql&logoColor=white) **PostgreSQL** (Produção)
- ![SQLite](https://img.shields.io/badge/SQLite-07405E?style=flat&logo=sqlite&logoColor=white) **SQLite** (Desenvolvimento)

### **Deploy & Infraestrutura**
- ![Render](https://img.shields.io/badge/Render-46E3B7?style=flat&logo=render&logoColor=white) **Render**
- ![Gunicorn](https://img.shields.io/badge/Gunicorn-499848?style=flat&logo=gunicorn&logoColor=white) **Gunicorn**
- ![WhiteNoise](https://img.shields.io/badge/WhiteNoise-FF6B6B?style=flat) **WhiteNoise**

---

## 📦 Principais Dependências

```txt
Django==5.1.7              # Framework web principal
gunicorn==23.0.0            # Servidor WSGI para produção
psycopg2-binary==2.9.10     # Driver PostgreSQL
pillow==11.1.0              # Processamento de imagens
whitenoise==6.9.0           # Servir arquivos estáticos
dj-database-url==2.3.0      # Configuração de database via URL
python-dotenv==1.1.0        # Gerenciamento de variáveis de ambiente
```

---

## 🎯 Funcionalidades

### 👤 **Seção Sobre Mim**
- Apresentação pessoal e profissional
- Foto de perfil e informações de contato
- História e objetivos de carreira

### 💻 **Habilidades Técnicas**
- Showcase de tecnologias dominadas
- Níveis de proficiência
- Categorização por áreas (Frontend, Backend, etc.)

### 🚀 **Portfólio de Projetos**
- Galeria de projetos desenvolvidos
- Descrições detalhadas e tecnologias utilizadas
- Links para repositórios e demos online

### 📞 **Contato & Serviços**
- Formulário de contato integrado
- Informações sobre serviços prestados
- Links para redes sociais e perfis profissionais

### 🔧 **Painel Administrativo**
- Interface Django Admin personalizada
- Gerenciamento completo de conteúdo
- Upload de imagens e documentos

---

## 🌐 Deploy

O projeto está configurado para deploy automático no **Render**:

### **Configurações de Produção**
- ✅ Coleta automática de arquivos estáticos
- ✅ Configuração do PostgreSQL
- ✅ Variáveis de ambiente seguras
- ✅ Servidor Gunicorn otimizado

### **Variáveis de Ambiente Necessárias**
```env
SECRET_KEY=sua_chave_secreta_forte
DEBUG=False
DATABASE_URL=postgresql://user:pass@host/db
ALLOWED_HOSTS=seu-dominio.com
```

---

## 📂 Estrutura do Projeto

```
portfolio_davi_oliveira/
├── 📁 static/              # Arquivos estáticos (CSS, JS, imagens)
├── 📁 templates/           # Templates HTML
├── 📁 media/              # Uploads de usuário
├── 📁 portfolio/          # App principal
│   ├── 📄 models.py       # Modelos de dados
│   ├── 📄 views.py        # Lógica das views
│   ├── 📄 urls.py         # Rotas da aplicação
│   └── 📄 admin.py        # Configuração do admin
├── 📄 manage.py           # Script de gerenciamento Django
├── 📄 requirements.txt    # Dependências do projeto
└── 📄 README.md          # Documentação
```

---

## 🤝 Contribuição

Contribuições são sempre bem-vindas! Para contribuir:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

---

<div align="center">
  <p>💡 <strong>Desenvolvido por Davi Oliveira - Software Engineer </strong></p>
  <p>⭐ Se este projeto te ajudou, considere dar uma estrela no repositório!</p>
</div>