from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("name", "email", "message")
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Seu nome"}),
            "email": forms.EmailInput(attrs={"placeholder": "seu@email.com"}),
            "message": forms.Textarea(
                attrs={"placeholder": "Escreva sua mensagem...", "rows": 6}
            ),
        }
