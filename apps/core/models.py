from django.db import models
from django.utils.translation import gettext_lazy as _


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
