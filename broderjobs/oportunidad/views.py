from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin
from . import forms
from django.views.generic import TemplateView, FormView
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.generic import UpdateView, CreateView
from django.views.generic import TemplateView, FormView
from django.core.urlresolvers import reverse_lazy
from .models import Oportunidad
from models import Persona, GradoEstudio, Universidad, Carrera, Pais, Ciudad, TipoPuesto, Idioma, CargaHoraria, TipoRemuneracion, Beneficio, Conocimiento
from empresa.models import Representante, Empresa


# Create your views here.
class OportunidadCrearView(FormView):
    form_class = forms.OportunidadForm
    template_name = 'oportunidad/crear.html'
    print("entro perfil")
    success_url = reverse_lazy('empresa-oportunidad-listar')

    def form_valid(self, form):
        user = self.request.user
        persona = get_object_or_404(Persona, usuario_id=user.id)
        representante =get_object_or_404(Representante, persona_id=persona.id)
        empresa = get_object_or_404(Empresa, id=representante.empresa.id)

        titulo = form.cleaned_data['titulo']
        carga_horaria = form.cleaned_data['carga_horaria']
        pais = form.cleaned_data['pais']
        ciudad = form.cleaned_data['ciudad']
        remuneracion = form.cleaned_data['remuneracion']
        fecha_cese = form.cleaned_data['fecha_cese']
        resumen = form.cleaned_data['resumen']
        beneficio = form.cleaned_data['beneficio']
        tipo_puesto = form.cleaned_data['tipo_puesto']

        grado_estudio = form.cleaned_data['grado_estudio']
        universidad = form.cleaned_data['universidad']
        carrera = form.cleaned_data['carrera']
        idioma = form.cleaned_data['idioma']
        conocimiento = form.cleaned_data['conocimiento']

        oportunidad = Oportunidad()
        oportunidad.empresa = empresa
        oportunidad.titulo = titulo
        oportunidad.carga_horaria  = carga_horaria
        oportunidad.pais = pais
        oportunidad.ciudad = ciudad
        oportunidad.remuneracion = remuneracion
        if fecha_cese is not None:
            oportunidad.fecha_cese = fecha_cese
        oportunidad.tipo_puesto = tipo_puesto
        oportunidad.grado_estudio = grado_estudio
        oportunidad.resumen = resumen
        oportunidad.save()

        oportunidad.universidad = universidad
        oportunidad.carrera = carrera
        oportunidad.idioma = idioma
        oportunidad.conocimiento = conocimiento
        oportunidad.estado = 'A'
        print(beneficio)
        oportunidad.beneficio = beneficio
        if '_guardar' in self.request.POST:
            oportunidad.estado = 'P'
        elif '_anunciar' in self.request.POST:
            oportunidad.estado = 'A'

        oportunidad.save()
        return super(OportunidadCrearView, self).form_valid(form)

class OportunidadEditarView(UpdateView):
    form_class = forms.OportunidadForm
    template_name = 'oportunidad/editar.html'
    success_url = reverse_lazy('empresa-oportunidad-listar')

    def get_object(self, queryset=None):
        id = self.kwargs["id"]
        oportunidad = Oportunidad.objects.get(pk = id)

        return oportunidad

    def form_valid(self, form):
        estado =  form.cleaned_data['estado_oportunidad']
        titulo = form.cleaned_data['titulo']
        carga_horaria = form.cleaned_data['carga_horaria']
        pais = form.cleaned_data['pais']
        ciudad = form.cleaned_data['ciudad']
        remuneracion = form.cleaned_data['remuneracion']
        fecha_cese = form.cleaned_data['fecha_cese']
        beneficio = form.cleaned_data['beneficio']
        tipo_puesto = form.cleaned_data['tipo_puesto']
        resumen = form.cleaned_data['resumen']
        grado_estudio = form.cleaned_data['grado_estudio']
        universidad = form.cleaned_data['universidad']
        carrera = form.cleaned_data['carrera']
        idioma = form.cleaned_data['idioma']
        conocimiento = form.cleaned_data['conocimiento']
        id = self.kwargs["id"]
        oportunidad = Oportunidad.objects.get(id = id)

        oportunidad.estado_oportunidad = estado
        oportunidad.estado = 'A'
        oportunidad.titulo = titulo
        oportunidad.carga_horaria  = carga_horaria
        oportunidad.pais = pais
        oportunidad.ciudad = ciudad
        oportunidad.remuneracion = remuneracion
        if fecha_cese is not None:
            oportunidad.fecha_cese = fecha_cese
        oportunidad.resumen = resumen
        oportunidad.tipo_puesto = tipo_puesto
        oportunidad.grado_estudio = grado_estudio
        oportunidad.save()

        oportunidad.universidad = universidad
        oportunidad.carrera = carrera
        oportunidad.idioma = idioma
        oportunidad.conocimiento = conocimiento
        oportunidad.beneficio = beneficio
        oportunidad.save()
        return super(OportunidadEditarView, self).form_valid(form)
