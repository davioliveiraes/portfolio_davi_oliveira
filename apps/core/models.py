from django.db import models
from django.utils.translation import get_language
from django.utils.translation import gettext_lazy as _


class TranslatableMixin:
    """Resolve campos PT/EN: retorna o campo `_en` quando o idioma ativo é
    inglês e há tradução preenchida; caso contrário, o campo em português."""

    def i18n(self, field):
        if (get_language() or "").startswith("en"):
            return getattr(self, f"{field}_en") or getattr(self, field)
        return getattr(self, field)


class Contact(models.Model):
    name = models.CharField(_("Nome"), max_length=150)
    email = models.EmailField(_("Email"))
    message = models.TextField(_("Mensagem"))
    read = models.BooleanField(_("Lida"), default=False)
    created_at = models.DateTimeField(_("Enviado em"), auto_now_add=True)

    class Meta:
        verbose_name = _("Mensagem")
        verbose_name_plural = _("Mensagens")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.email}"


class SkillCategory(TranslatableMixin, models.Model):
    name = models.CharField(_("Nome"), max_length=100)
    name_en = models.CharField(_("Nome (EN)"), max_length=100, blank=True)
    icon = models.CharField(
        _("Ícone"), max_length=50, help_text="Classe Font Awesome, ex: fas fa-server"
    )
    order = models.PositiveSmallIntegerField(_("Ordem"), default=0)

    class Meta:
        verbose_name = _("Categoria de competência")
        verbose_name_plural = _("Categorias de competências")
        ordering = ["order", "id"]

    def __str__(self):
        return self.name

    @property
    def name_i18n(self):
        return self.i18n("name")


class Skill(TranslatableMixin, models.Model):
    category = models.ForeignKey(
        SkillCategory,
        on_delete=models.CASCADE,
        related_name="skills",
        verbose_name=_("Categoria"),
    )
    name = models.CharField(_("Nome"), max_length=100)
    name_en = models.CharField(_("Nome (EN)"), max_length=100, blank=True)
    detail = models.CharField(_("Detalhe"), max_length=150, blank=True)
    detail_en = models.CharField(_("Detalhe (EN)"), max_length=150, blank=True)
    icon = models.CharField(
        _("Ícone"), max_length=50, help_text="Classe Font Awesome, ex: fab fa-python"
    )
    order = models.PositiveSmallIntegerField(_("Ordem"), default=0)

    class Meta:
        verbose_name = _("Competência")
        verbose_name_plural = _("Competências")
        ordering = ["order", "id"]

    def __str__(self):
        return self.name

    @property
    def name_i18n(self):
        return self.i18n("name")

    @property
    def detail_i18n(self):
        return self.i18n("detail")


class Project(TranslatableMixin, models.Model):
    title = models.CharField(_("Título"), max_length=150)
    title_en = models.CharField(_("Título (EN)"), max_length=150, blank=True)
    description = models.TextField(_("Descrição"))
    description_en = models.TextField(_("Descrição (EN)"), blank=True)
    tags = models.CharField(
        _("Tags"), max_length=255, help_text="Separadas por vírgula"
    )
    tags_en = models.CharField(_("Tags (EN)"), max_length=255, blank=True)
    github_url = models.URLField(_("URL do GitHub"))
    live_url = models.URLField(_("URL do site no ar"), blank=True)
    order = models.PositiveSmallIntegerField(_("Ordem"), default=0)

    class Meta:
        verbose_name = _("Projeto")
        verbose_name_plural = _("Projetos")
        ordering = ["order", "id"]

    def __str__(self):
        return self.title

    @property
    def title_i18n(self):
        return self.i18n("title")

    @property
    def description_i18n(self):
        return self.i18n("description")

    @property
    def tag_list(self):
        return [t.strip() for t in self.i18n("tags").split(",") if t.strip()]

    @property
    def repo_name(self):
        """Nome do repositório extraído da URL, para casar com a API do GitHub."""
        return self.github_url.rstrip("/").rsplit("/", 1)[-1]


class Experience(TranslatableMixin, models.Model):
    role = models.CharField(_("Cargo"), max_length=150)
    role_en = models.CharField(_("Cargo (EN)"), max_length=150, blank=True)
    company = models.CharField(_("Empresa"), max_length=150)
    company_url = models.URLField(_("Site da empresa"), blank=True)
    period = models.CharField(_("Período"), max_length=150)
    period_en = models.CharField(_("Período (EN)"), max_length=150, blank=True)
    details = models.TextField(_("Atividades"), help_text="Uma por linha")
    details_en = models.TextField(_("Atividades (EN)"), blank=True)
    skills = models.CharField(_("Habilidades"), max_length=255, blank=True)
    skills_en = models.CharField(_("Habilidades (EN)"), max_length=255, blank=True)
    order = models.PositiveSmallIntegerField(_("Ordem"), default=0)

    class Meta:
        verbose_name = _("Experiência")
        verbose_name_plural = _("Experiências")
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.role} - {self.company}"

    @property
    def role_i18n(self):
        return self.i18n("role")

    @property
    def period_i18n(self):
        return self.i18n("period")

    @property
    def skills_i18n(self):
        return self.i18n("skills")

    @property
    def details_list(self):
        return [d.strip() for d in self.i18n("details").splitlines() if d.strip()]


class Certification(TranslatableMixin, models.Model):
    name = models.CharField(_("Nome"), max_length=200)
    name_en = models.CharField(_("Nome (EN)"), max_length=200, blank=True)
    institution = models.CharField(_("Instituição"), max_length=150)
    hours = models.PositiveSmallIntegerField(
        _("Carga horária (h)"), null=True, blank=True
    )
    order = models.PositiveSmallIntegerField(_("Ordem"), default=0)

    class Meta:
        verbose_name = _("Certificação")
        verbose_name_plural = _("Certificações")
        ordering = ["order", "id"]

    def __str__(self):
        return self.name

    @property
    def name_i18n(self):
        return self.i18n("name")
