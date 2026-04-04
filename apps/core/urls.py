from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("sobre/", views.sobre, name="sobre"),
    path("competencias/", views.competencias, name="competencias"),
    path("projetos/", views.projetos, name="projetos"),
    path("experiencias/", views.experiencias, name="experiencias"),
    path("formacao/", views.formacao, name="formacao"),
    path("contato/", views.contato, name="contato"),
]
