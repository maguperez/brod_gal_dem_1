import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin
from . import forms
from django.http import Http404
from django.http import JsonResponse
from django.contrib.auth import views
#from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, FormView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView,CreateView, DeleteView
from .models import Estudiante, Resumen, ActividadesExtra, ExperienciaProfesional, Voluntariado
from main.models import Persona, GradoEstudio, Universidad, Carrera, Pais, Ciudad, TipoPuesto, Idioma
from empresa.models import Puesto, Empresa, Sector
from main import utilitarios



@login_required(login_url='/estudiante-registro/')
def registro_cv(request):

    if request.method == 'POST':
        form = forms.RegistroCVForm(request.POST)
        if form.is_valid():
            user = request.user
            persona = Persona.objects.get(usuario_id=user.id)
            grado_estudio = form.cleaned_data['grado_estudio']
            universidad = form.cleaned_data['universidad']
            carrera = form.cleaned_data['carrera']
            pais = form.cleaned_data['pais']
            ciudad = form.cleaned_data['ciudad']
            tipo_puesto = form.cleaned_data['tipo_puesto']
            ano_inicio = form.cleaned_data['ano_inicio_estudio']
            semestre_inicio = form.cleaned_data['semestre_inicio_estudio']
            ano_graduacion = form.cleaned_data['ano_graduacion']
            semestre_graduacion = form.cleaned_data['semestre_graduacion']

            estudiante = Estudiante()
            estudiante.persona = persona
            estudiante.grado_estudio = grado_estudio
            estudiante.universidad = universidad
            estudiante.carrera = carrera
            estudiante.pais = pais
            estudiante.ciudad = ciudad
            estudiante.ano_inicio_estudio = ano_inicio
            estudiante.semestre_inicio_estudio = semestre_inicio
            estudiante.ano_graduacion = ano_graduacion
            estudiante.semestre_graduacion = semestre_graduacion
            estudiante.save()

            estudiante.tipo_puesto = tipo_puesto
            estudiante.save()

            resumen = Resumen()
            resumen.estudiante = estudiante
            resumen.save()

            return redirect('oportunidad_listar')
    else:
        form = forms.RegistroCVForm()
    return render(request, 'estudiante/registro-cv.html', {'form': form})

@login_required(login_url='/estudiante-registro/')
def oportunidad_listar(request):
    return render(request, 'estudiante/oportunidad-listar.html')

class ConfiguracionView(TemplateView):

    template_name = 'estudiante/configuracion.html'
    def get_context_data(self, **kwargs):
        user = self.request.user
        usuario = User.objects.get(pk=user.id)
        persona = Persona.objects.get(usuario_id=usuario.id)

        context = super(ConfiguracionView, self).get_context_data(**kwargs)
        context['usuario'] = user
        context['persona'] = persona
        return context

class EditarCuentaView(TemplateView):

    template_name = 'estudiante/editar-cuenta.html'

class EmpresaListaView(TemplateView):

    template_name = 'estudiante/empresa-lista.html'

class EmpresaDetalleView(TemplateView):

    template_name = 'estudiante/empresa-detalle.html'
    def get_context_data(self, **kwargs):
        id = kwargs.get('id', None)
        empresa = get_object_or_404(Empresa, pk=id)
        context = super(EmpresaDetalleView, self).get_context_data(**kwargs)
        context['empresa'] = empresa
        return context

class EmpresaBusquedaView(TemplateView):
    def get(self, request, *args, **kwargs):
        busqueda = request.GET['busqueda']
        empresas = Empresa.objects.filter(nombre__icontains=busqueda)
        a_empresas =[]
        for i in range(0, len(empresas)):
            sector = empresas[i].nombre
            if empresas[i].sector is not None:
                sector = Sector.objects.get(id=empresas[i].sector.id).descripcion
            e = {
                "id": empresas[i].id,
                "nombre": empresas[i].nombre,
                "logo": empresas[i].set_logo,
                "sector": sector,
                "ranking_general": empresas[i].ranking_general,
            }
            a_empresas.append(e)
        # data = serializers.serialize('json', a_empresas,
        #                              fields=('id','nombre', 'sector', 'logo', 'ranking_general' ))
        data = json.dumps(a_empresas)
        return HttpResponse(data, content_type='application/json')

class MiCVView(TemplateView):

    template_name = 'estudiante/mi-cv.html'
    def get_context_data(self, **kwargs):
        user = self.request.user
        persona = Persona.objects.get(usuario_id=user.id)
        estudiante = Estudiante.objects.get(persona_id=persona.id)
        edad = utilitarios.calular_edad(persona.fecha_nacimiento)
        context = super(MiCVView, self).get_context_data(**kwargs)
        context['usuario'] = user
        context['persona'] = persona
        context['estudiante'] = estudiante
        context['edad'] = edad
        context['resumen'] = Resumen.objects.get(estudiante_id=estudiante.id)
        context['actividades_extra'] = ActividadesExtra.objects.filter(estudiante_id=estudiante.id)
        context['experiencias_profesionales'] = ExperienciaProfesional.objects.filter(estudiante_id=estudiante.id)
        context['voluntariados'] = Voluntariado.objects.filter(estudiante_id=estudiante.id)
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

class FotoView(SuccessMessageMixin, AjaxTemplateMixin, UpdateView):
    form_class = forms.FotoForm
    template_name = 'estudiante/mi-cv-foto.html'
    success_url =reverse_lazy('mi_cv')

    def get_object(self, queryset=None):
        user = self.request.user
        persona = Persona.objects.get(usuario_id=user.id)
        estudiante = Estudiante.objects.get(persona_id =persona.id)
        return estudiante

    def form_valid(self, form):

        user = self.request.user
        persona = Persona.objects.get(usuario_id=user.id)
        estudiante = Estudiante.objects.get(persona_id=persona.id)
        estudiante.foto = self.request.FILES['foto']
        estudiante.save()
        return super(FotoView, self).form_valid(form)

class InfoPersonalView(SuccessMessageMixin, AjaxTemplateMixin,UpdateView):
    form_class =forms.InfoPersonalForm
    template_name = 'estudiante/mi-cv-info-personal.html'
    success_url = reverse_lazy('mi_cv')

    def get_object(self, queryset=None):
        user = self.request.user
        persona = Persona.objects.get(usuario_id=user.id)
        estudiante = Estudiante.objects.get(persona_id =persona.id)
        return estudiante

    def get_initial(self):
        user = self.request.user
        usuario = User.objects.get(pk = user.id)
        persona = Persona.objects.get(usuario_id=user.id)
        return {
            'email': usuario.email,
            'telefono': persona.telefono,
            'fecha_nacimiento': persona.fecha_nacimiento}

    def form_valid(self, form):
        user = self.request.user
        usuario = User.objects.get(pk = user.id)
        persona = Persona.objects.get(usuario_id=user.id)
        grado_estudio = form.cleaned_data['grado_estudio']
        universidad = form.cleaned_data['universidad']
        carrera = form.cleaned_data['carrera']
        pais =  form.cleaned_data['pais']
        ciudad = form.cleaned_data['ciudad']
        ano_inicio = form.cleaned_data['ano_inicio_estudio']
        semestre_inicio = form.cleaned_data['semestre_inicio_estudio']
        ano_graduacion = form.cleaned_data['ano_graduacion']
        semestre_graduacion = form.cleaned_data['semestre_graduacion']

        estudiante = Estudiante.objects.get(persona_id=persona.id)
        estudiante.grado_estudio = grado_estudio
        estudiante.universidad = universidad
        estudiante.carrera = carrera
        estudiante.pais = pais
        estudiante.ciudad = ciudad
        estudiante.ano_inicio_estudio = ano_inicio
        estudiante.semestre_inicio_estudio = semestre_inicio
        estudiante.ano_graduacion = ano_graduacion
        estudiante.semestre_graduacion = semestre_graduacion

        fecha = form.cleaned_data['fecha_nacimiento']
        usuario.email = form.cleaned_data['email']
        persona.telefono = form.cleaned_data['telefono']
        if fecha is not None:
            persona.fecha_nacimiento= fecha
        usuario.save()
        persona.save()
        estudiante.save()
        return super(InfoPersonalView, self).form_valid(form)

class ResumenView(SuccessMessageMixin, AjaxTemplateMixin, FormView):
    template_name = 'estudiante/mi-cv-resumen.html'
    form_class = forms.ResumenForm
    success_url = reverse_lazy('mi_cv')
    success_message = "Guardado con exito!"

    def get_initial(self):
        user = self.request.user
        persona = Persona.objects.get(usuario_id=user.id)
        estudiante = Estudiante.objects.get(persona_id=persona.id)
        resumen = Resumen.objects.get(estudiante_id=estudiante.id)
        return {'resumen': resumen.descripcion}

    def form_valid(self, form):
        user = self.request.user
        persona = Persona.objects.get(usuario_id=user.id)
        estudiante = Estudiante.objects.get(persona_id=persona.id)
        resumen = Resumen.objects.get(estudiante_id=estudiante.id)
        resumen.descripcion = form.cleaned_data['resumen']

        resumen.save()
        return super(ResumenView, self).form_valid(form)

class DisponibilidadView(SuccessMessageMixin, AjaxTemplateMixin, UpdateView):
    template_name = 'estudiante/mi-cv-disponibilidad.html'
    form_class = forms.DisponibilidadForm
    success_url = reverse_lazy('mi_cv')
    success_message = "Guardado con exito!"

    def get_object(self, queryset=None):
        user = self.request.user
        persona = Persona.objects.get(usuario_id=user.id)
        estudiante = Estudiante.objects.get(persona_id =persona.id)
        return estudiante

    def form_valid(self, form):
        user = self.request.user
        persona = Persona.objects.get(usuario_id=user.id)
        estudiante = Estudiante.objects.get(persona_id=persona.id)
        tipo_puesto = form.cleaned_data['tipo_puesto']
        estudiante.tipo_puesto = tipo_puesto
        estudiante.save()
        return super(DisponibilidadView, self).form_valid(form)

class IdiomaView(SuccessMessageMixin, AjaxTemplateMixin, FormView):
    template_name = 'estudiante/mi-cv-idioma.html'
    form_class = forms.IdiomaForm
    success_url = reverse_lazy('mi_cv')
    success_message = "Guardado con exito!"

    def form_valid(self, form):
        user = self.request.user
        persona = Persona.objects.get(usuario_id=user.id)
        estudiante = Estudiante.objects.get(persona_id=persona.id)
        idioma = form.cleaned_data['idioma']
        estudiante.idioma = idioma
        estudiante.save()
        return super(IdiomaView, self).form_valid(form)

class ConocimientoView(SuccessMessageMixin, AjaxTemplateMixin, FormView):
    template_name = 'estudiante/mi-cv-conocimiento.html'
    form_class = forms.ConocimientoForm
    success_url = reverse_lazy('mi_cv')
    success_message = "Guardado con exito!"

    def form_valid(self, form):
        user = self.request.user
        persona = Persona.objects.get(usuario_id=user.id)
        estudiante = Estudiante.objects.get(persona_id=persona.id)
        conocimiento = form.cleaned_data['conocimiento']
        estudiante.conocimiento = conocimiento
        estudiante.save()
        return super(ConocimientoView, self).form_valid(form)

class ExperienciaView(SuccessMessageMixin, AjaxTemplateMixin,UpdateView):
    template_name = 'estudiante/mi-cv-experiencia-editar.html'
    form_class = forms.ExperienciaForm
    success_url = reverse_lazy('mi_cv')
    success_message = "Guardado con exito!"

    def get_object(self, queryset=None):
        id = self.kwargs["id"]
        print(id)
        experiencia = get_object_or_404(ExperienciaProfesional, id= id)
        return experiencia



class ExperienciaCrearView(SuccessMessageMixin, AjaxTemplateMixin,CreateView):
    form_class = forms.ExperienciaForm
    template_name = 'estudiante/mi-cv-experiencia-crear.html'
    success_url = reverse_lazy('mi_cv')

    def form_valid(self, form):
        user = self.request.user
        usuario = User.objects.get(pk = user.id)
        persona = Persona.objects.get(usuario_id=user.id)
        estudiante = Estudiante.objects.get(persona_id=persona.id)
        experiencia = ExperienciaProfesional()
        puesto = form.cleaned_data['puesto']
        empresa = form.cleaned_data['empresa']
        fecha_desde = form.cleaned_data['fecha_desde']
        fecha_hasta = form.cleaned_data['fecha_hasta']
        descripcion = form.cleaned_data['descripcion']
        experiencia.estudiante = estudiante
        experiencia.puesto = puesto
        experiencia.empresa = empresa
        if fecha_desde is not None:
            experiencia.fecha_desde = fecha_desde
        if fecha_hasta is not None:
            experiencia.fecha_hasta = fecha_hasta
            experiencia.trabajo_actual = 'N'
        else:
            experiencia.trabajo_actual = 'S'
        experiencia.descripcion = descripcion
        experiencia.save()
        return super(ExperienciaCrearView, self).form_valid(form)

class ExperienciaEliminarView(DeleteView):

    def get_object(self, queryset=None):
        experiencia = ExperienciaProfesional.objects.get(id =self.request.GET.get('id'))
        return experiencia
        if experiencia is None:
            raise Http404
        return ex4

class VoluntariadoView(SuccessMessageMixin, AjaxTemplateMixin,UpdateView):
    form_class = forms.VoluntariadoForm
    template_name = 'estudiante/mi-cv-voluntariado-editar.html'
    success_url = reverse_lazy('mi_cv')

    def get_object(self, queryset=None):
        voluntariado = Voluntariado.objects.get(id =self.request.GET.get('id'))
        return voluntariado
    
class VoluntariadoCrearView(SuccessMessageMixin, AjaxTemplateMixin,CreateView):
    form_class = forms.VoluntariadoForm
    template_name = 'estudiante/mi-cv-voluntariado-crear.html'
    success_url = reverse_lazy('mi_cv')

    def form_valid(self, form):
        user = self.request.user
        usuario = User.objects.get(pk = user.id)
        persona = Persona.objects.get(usuario_id=user.id)
        estudiante = Estudiante.objects.get(persona_id=persona.id)
        voluntariado = Voluntariado()
        puesto = form.cleaned_data['cargo']
        empresa = form.cleaned_data['organizacion']
        fecha_desde = form.cleaned_data['fecha_desde']
        fecha_hasta = form.cleaned_data['fecha_hasta']
        descripcion = form.cleaned_data['descripcion']
        voluntariado.estudiante = estudiante
        voluntariado.puesto = puesto
        voluntariado.empresa = empresa
        if fecha_desde is not None:
            voluntariado.fecha_desde = fecha_desde
        if fecha_hasta is not None:
            voluntariado.fecha_hasta = fecha_hasta
            voluntariado.voluntariado_actual = 'N'
        else:
            voluntariado.voluntariado_actual = 'S'
        voluntariado.descripcion = descripcion
        voluntariado.save()
        return super(VoluntariadoCrearView, self).form_valid(form)

class VoluntariadoEliminarView(DeleteView):

    def get_object(self, queryset=None):
        voluntariado = ExperienciaProfesional.objects.get(id =self.request.GET.get('id'))
        return voluntariado
        if voluntariado is None:
            raise Http404
        return ex4