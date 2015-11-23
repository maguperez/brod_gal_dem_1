from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response, redirect
from django.contrib.messages.views import SuccessMessageMixin
from . import forms
from django.views.generic import TemplateView, FormView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import UpdateView
from django.views.generic import TemplateView, FormView
from django.core.urlresolvers import reverse_lazy
from .models import Puesto, Empresa, Representante, Sector
from main.models import Persona, Universidad, Carrera, Pais, Ciudad, TipoPuesto, Idioma
from oportunidad.models import Oportunidad


# Create your views here.
@login_required(login_url='/empresa-registro/')
def oportunidad_listar(request):
    return render(request, 'empresa/oportunidades-listar.html')

class ConfiguracionView(TemplateView):

    template_name = 'empresa/configuracion.html'
    def get_context_data(self, **kwargs):
        user = self.request.user
        usuario = User.objects.get(pk=user.id)
        context = super(ConfiguracionView, self).get_context_data(**kwargs)
        context['usuario'] = user
        return context

class MiEmpresaView(TemplateView):
    template_name = 'empresa/mi-empresa.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        persona = Persona.objects.get(usuario_id=user.id)
        representante = Representante.objects.get(persona_id =persona.id)
        empresa = Empresa.objects.get(id=representante.empresa.id)
        oportunidades =  Oportunidad.objects.filter(empresa_id = empresa.id)
        context = super(MiEmpresaView, self).get_context_data(**kwargs)
        context['empresa'] = empresa
        context['oportunidades'] = oportunidades
        return context

class AjaxTemplateMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not hasattr(self, 'ajax_template_name'):
            split = self.template_name.split('.html')
            #split[-1] = '-inner'
            split.append('.html')
            self.ajax_template_name = ''.join(split)
            if request.is_ajax():
                self.template_name = self.ajax_template_name
            return super(AjaxTemplateMixin, self).dispatch(request, *args, **kwargs)

class InfoGeneralView(SuccessMessageMixin, AjaxTemplateMixin,UpdateView):

        form_class = forms.InfoGeneralForm
        template_name = 'empresa/mi-empresa-info-general.html'
        success_url = reverse_lazy('mi-empresa')

        #get object
        def get_object(self, queryset=None):
            user = self.request.user
            persona = Persona.objects.get(usuario_id=user.id)
            representante = Representante.objects.get(persona_id =persona.id)
            empresa = Empresa.objects.get(id=representante.empresa.id)
            return empresa

class LogoView(SuccessMessageMixin, AjaxTemplateMixin,UpdateView):
    form_class = forms.LogoForm
    template_name = 'empresa/mi-empresa-logo.html'
    success_url = reverse_lazy('mi-empresa')

    def get_object(self, queryset=None):
        user = self.request.user
        persona = Persona.objects.get(usuario_id=user.id)
        representante = Representante.objects.get(persona_id =persona.id)
        empresa = Empresa.objects.get(id=representante.empresa.id)
        return empresa

class OportunidadListarView(TemplateView):
    template_name = 'empresa/oportunidad-listar.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        persona = Persona.objects.get(usuario_id=user.id)
        representante = Representante.objects.get(persona_id =persona.id)
        empresa = Empresa.objects.get(id=representante.empresa.id)
        oportunidades =  Oportunidad.objects.filter(empresa_id = empresa.id)
        context = super(OportunidadListarView, self).get_context_data(**kwargs)
        context['empresa'] = empresa
        context['oportunidades'] = oportunidades
        return context