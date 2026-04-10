from django.db import models


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
