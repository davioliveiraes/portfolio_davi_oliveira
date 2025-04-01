from django.urls import path
from .views import HomeTemplateView, Contato

urlpatterns = [
    path("", HomeTemplateView.as_view()),
    path("contato/", Contato, name="contato"),
]
