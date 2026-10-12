from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Contact


class ContactForm(forms.ModelForm):
    # Honeypot: escondido de quem usa o site, mas bots preenchem todo campo
    website = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"tabindex": "-1", "autocomplete": "off"}),
    )

    class Meta:
        model = Contact
        fields = ("name", "email", "message")
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": _("Seu nome")}),
            "email": forms.EmailInput(attrs={"placeholder": _("seu@email.com")}),
            "message": forms.Textarea(
                attrs={"placeholder": _("Escreva sua mensagem..."), "rows": 6}
            ),
        }

    def is_spam(self):
        return bool(self.cleaned_data.get("website"))
