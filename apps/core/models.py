from django.db import models


class Project(models.Model):
    title = models.CharField("Título", max_length=200)
    description = models.TextField("Descrição")
    image = models.ImageField("Imagem", upload_to="projects/", blank=True)
    technologies = models.CharField(
        "Tecnologias", max_length=300, help_text="Separadas por vírgula"
    )
    github_url = models.URLField("GitHub", blank=True)
    demo_url = models.URLField("Demo", blank=True)
    featured = models.BooleanField("Destaque", default=False)
    created_at = models.DateTimeField("Criado em", auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True)

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"
        ordering = ["-featured", "-created_at"]

    def __str__(self):
        return self.title

    def tech_list(self):
        return [tech.strip() for tech in self.technologies.split(",")]


class Contact(models.Model):
    name = models.CharField("Nome", max_length=150)
    email = models.EmailField("Email")
    message = models.TextField("Mensagem")
    read = models.BooleanField("Lida", default=False)
    created_at = models.DateTimeField("Enviado em", auto_now_add=True)

    class Meta:
        verbose_name = "Mensagem"
        verbose_name_plural = "Mensagens"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.email}"
