from django.views.generic import TemplateView
from .models import *
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

# Create your views here.
class HomeTemplateView(TemplateView):
   template_name = 'home.html'

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['about'] = About.objects.first()
      context['services'] = Service.objects.all()
      context['works'] = RecentWork.objects.all()
      return context

def Contato(request):
   if request.method == "POST":
      nome = request.POST.get('name')
      email = request.POST.get('email')
      mensagem = request.POST.get('message')

      assunto = f"Mensagem de {nome}"
      corpo_mensagem = f"Nome: {nome}\nEmail: {email}\n\nMessagem:\n {mensagem}"

      try:
         send_mail(
            assunto,
            corpo_mensagem,
            email,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
         )
         messages.success(request, "Mensagem enviada com sucesso!")
      except Exception as e:
         messages.error(request, f"Erro ao enviar mensagem: {e}")
      
      return redirect('contato')

   return render(request, 'home.html')
   