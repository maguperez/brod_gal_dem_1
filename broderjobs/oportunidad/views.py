from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response, redirect
from django.contrib.messages.views import SuccessMessageMixin
from . import forms
from django.views.generic import TemplateView, FormView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import UpdateView, CreateView
from django.views.generic import TemplateView, FormView
from django.core.urlresolvers import reverse_lazy
from .models import Oportunidad, PerfilOportunidad
from models import Persona, GradoEstudio, Universidad, Carrera, Pais, Ciudad, TipoPuesto, Idioma, CargaHoraria, TipoRemuneracion, Beneficio, Conocimiento
from empresa.models import Representante, Empresa


# Create your views here.
class OportunidadCrearView(FormView):
    form_class = forms.OportunidadCrearForm
    template_name = 'oportunidad/crear.html'
    print("entro perfil")
    success_url = reverse_lazy('empresa_oportunidad_listar')

    def form_valid(self, form):
        user = self.request.user
        persona = Persona.objects.get(usuario_id=user.id)
        representante = Representante.objects.get(persona_id=persona.id)
        empresa = Empresa.objects.get(id=representante.empresa.id)

        titulo = form.cleaned_data['titulo']
        carga_horaria = form.cleaned_data['carga_horaria']
        pais = form.cleaned_data['pais']
        ciudad = form.cleaned_data['ciudad']
        remuneracion = form.cleaned_data['remuneracion']
        fecha_cese = form.cleaned_data['fecha_cese']
        beneficio = form.cleaned_data['beneficio']
        tipo_puesto = form.cleaned_data['tipo_puesto']

        grado_estudio = form.cleaned_data['grado_estudio']
        universidad = form.cleaned_data['universidad']
        carrera = form.cleaned_data['carrera']
        idioma = form.cleaned_data['idioma']
        conocimiento = form.cleaned_data['conocimiento']

        print("valido form")

        oportunidad = Oportunidad()
        oportunidad.empresa = empresa
        oportunidad.titulo = titulo
        oportunidad.carga_horaria  = carga_horaria
        oportunidad.pais = pais
        oportunidad.ciudad = ciudad
        oportunidad.remuneracion = remuneracion
        # oportunidad.beneficio = beneficio
        if fecha_cese is not None:
            oportunidad.fecha_cese = fecha_cese
        oportunidad.tipo_puesto = tipo_puesto

        perfil = PerfilOportunidad()
        perfil.grado_estudio = grado_estudio
        perfil.save()
        perfil.universidad = universidad
        perfil.carrera = carrera
        perfil.idioma = idioma
        perfil.conocimiento = conocimiento
        perfil.save()

        oportunidad.perfil_oportunidad = perfil
        print("asigno perfil")

        oportunidad.save()
        print("save")
        return super(OportunidadCrearView , self).form_valid(form)



