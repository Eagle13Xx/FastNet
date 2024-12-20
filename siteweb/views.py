from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.contrib import messages
from .models import Plano, PlanoAdquirido


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['planos'] = Plano.objects.all()
        return context


class PlanoDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'adquirir_plano.html'
    login_url = '/usuario/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        plano = get_object_or_404(Plano, id=kwargs['pk'])
        context['plano'] = plano
        return context

    def post(self, request, *args, **kwargs):
        plano = get_object_or_404(Plano, id=kwargs['pk'])
        PlanoAdquirido.objects.create(usuario=request.user, plano=plano)
        messages.success(request, f"Você adquiriu o plano {plano.nome} com sucesso!")
        return redirect('planos_adquiridos')



class PlanosAdquiridosView(LoginRequiredMixin, TemplateView):
    template_name = 'planos_adquiridos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['planos'] = PlanoAdquirido.objects.filter(usuario=self.request.user)
        return context
