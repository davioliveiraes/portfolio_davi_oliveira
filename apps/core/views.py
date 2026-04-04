from django.shortcuts import render


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
    return render(request, "core/contato.html")
