from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from .forms import ContactForm


def home(request):
    return render(request, "core/home.html")


def sobre(request):
    return render(request, "core/sobre.html")


def competencias(request):
    return render(request, "core/competencias.html")


def projetos(request):
    return render(request, "core/projetos.html")


def experiencias(request):
    return render(request, "core/experiencias.html")


def formacao(request):
    return render(request, "core/formacao.html")


def contato(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
                subject=f"[Portfólio] Nova mensagem de {form.cleaned_data['name']}",
                message=f"Nome: {form.cleaned_data['name']}\n"
                f"Email: {form.cleaned_data['email']}\n\n"
                f"{form.cleaned_data['message']}",
                from_email="davioliveiraes7@gmail.com",
                recipient_list=["davioliveiraes7@gmail.com"],
                fail_silently=False,
            )
            messages.success(
                request, "Mensagem enviada com sucesso! Obrigado pelo contato."
            )
            return redirect("core:contato")
        else:
            messages.error(
                request, "Erro ao enviar. Verifique os campos e tente novamente."
            )
    else:
        form = ContactForm()
    return render(request, "core/contato.html", {"form": form})
