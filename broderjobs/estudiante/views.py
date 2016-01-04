import json
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin
from . import forms
from django.db.models import Q
from django.http import Http404
from django.http import JsonResponse
from django.contrib.auth import views
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, FormView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView,CreateView, DeleteView
from datetime import date
from .models import Estudiante, Resumen, ActividadesExtra, ExperienciaProfesional, Voluntariado
from main.models import Persona, GradoEstudio, Universidad, Carrera, Pais, Ciudad, TipoPuesto, Idioma
from empresa.models import Puesto, Empresa, Sector, RankingEmpresa, EvaluacionEmpresa
from oportunidad.models import Oportunidad, Postulacion
from mensaje.models import Mensaje, Mensaje_Destinatario
from main import utils
from main.utils import LoginRequiredMixin
from empresa.utils import actualizar_ranking_empresa

@login_required(login_url='/estudiante-registro/')
def registro_cv(request):

    if request.method == 'POST':
        form = forms.RegistroCVForm(request.POST)
        if form.is_valid():
            user = request.user
            persona = get_object_or_404(Persona, usuario_id=user.id)
            grado_estudio = form.cleaned_data['grado_estudio']
            id_universidad = form.cleaned_data['universidades_hidden']
            id_carrera = form.cleaned_data['carreras_hidden']

            pais = form.cleaned_data['pais']

            # id_pais = form.cleaned_data['paises_hidden']

            # id_ciudad = form.cleaned_data['ciudades_hidden']
            id_ciudad = form.cleaned_data['ciudad_hidden']
            tipo_puesto = form.cleaned_data['tipo_puesto']
            ano_inicio = form.cleaned_data['ano_inicio_estudio']
            semestre_inicio = form.cleaned_data['semestre_inicio_estudio']
            ano_graduacion = form.cleaned_data['ano_graduacion']
            semestre_graduacion = form.cleaned_data['semestre_graduacion']
            carga_horaria = form.cleaned_data['carga_horaria']

            try:
                estudiante = Estudiante.objects.get(persona_id = persona.id)
            except Estudiante.DoesNotExist:
                estudiante = None
            if estudiante is None:
                estudiante = Estudiante()
                estudiante.persona = persona

            estudiante.grado_estudio = grado_estudio
            universidad = Universidad.objects.get(id= id_universidad )
            if universidad is not None:
                estudiante.universidad = universidad

            carrera = Carrera.objects.get(id = id_carrera)
            if carrera is not None:
                estudiante.carrera = carrera

            estudiante.pais = pais
            # pais = Pais.objects.get(id= id_pais)
            # if pais is not None:
            #     estudiante.pais = pais

            if id_ciudad is not None and id_ciudad != '':
                try:
                    ciudad = Ciudad.objects.get(id = id_ciudad)
                except Ciudad.DoesNotExist:
                    ciudad = None
                if ciudad is not None:
                    estudiante.ciudad = ciudad

            # ciudad = Ciudad.objects.get(id = id_ciudad)
            # if ciudad is not None:
            #     estudiante.ciudad = ciudad
            estudiante.ano_inicio_estudio = ano_inicio
            estudiante.semestre_inicio_estudio = semestre_inicio
            estudiante.ano_graduacion = ano_graduacion
            estudiante.semestre_graduacion = semestre_graduacion
            estudiante.carga_horaria = carga_horaria
            estudiante.save()

            estudiante.tipo_puesto = tipo_puesto
            estudiante.save()

            # resumen = Resumen(estudiante_id = estudiante.id)
            # if Resumen is None:
            #     resumen.estudiante = estudiante
            #     resumen.save()
            r, created = Resumen.objects.get_or_create(estudiante_id = estudiante.id)
            if created is True:
                r.save()

            return redirect('estudiante-oportunidad-listar')
    else:
        form = forms.RegistroCVForm()
    return render(request, 'estudiante/registro-cv.html', {'form': form})

@login_required(login_url='/estudiante-registro/')
def oportunidad_listar(request):
    return render(request, 'estudiante/oportunidad-listar.html')

class EmpresaDetalleView(LoginRequiredMixin, FormView):

    form_class = forms.EvaluacionForm
    template_name = 'estudiante/empresa-detalle.html'
    #success_url = reverse_lazy('estudiante-empresa-detalle')

    def get_context_data(self, **kwargs):
        id = self.kwargs['id']
        empresa = get_object_or_404(Empresa, pk=id)
        oportunidades =  Oportunidad.objects.filter(empresa_id = empresa.id, estado_oportunidad = 'A').order_by("fecha_publicacion")[:2]
        ranking = RankingEmpresa()
        try:
            ranking = RankingEmpresa.objects.get(empresa_id = empresa.id)

        except Estudiante.DoesNotExist:
            ranking.ranking_general = 0
            ranking.linea_carrera = 0
            ranking.flexibilidad_horarios = 0
            ranking.ambiente_trabajo = 0
            ranking.salarios = 0
        context = super(EmpresaDetalleView, self).get_context_data(**kwargs)
        context['empresa'] = empresa
        context['oportunidades'] = oportunidades
        context['ranking'] = ranking
        return context

    def form_valid(self, form):
        linea =  form.cleaned_data['linea_carrera']
        flexibilidad =  form.cleaned_data['flexibilidad_horarios']
        ambiente =  form.cleaned_data['ambiente_trabajo']
        salario =  form.cleaned_data['salarios']
        ranking = (linea + flexibilidad + ambiente + salario)/4
        id = self.kwargs['id']

        e, created = EvaluacionEmpresa.objects.get_or_create(empresa_id = id, usuario_id = self.request.user.id )
        e.linea_carrera = linea
        e.flexibilidad_horarios = flexibilidad
        e.ambiente_trabajo = ambiente
        e.salarios = salario
        e.ranking = ranking
        e.save()
        actualizar_ranking_empresa(id)
        return super(EmpresaDetalleView, self).form_valid(form)

    def get_success_url(self, **kwargs):
        id = self.kwargs['id']
        if id != None:
            #return reverse_lazy('estudiante-empresa-lista')
            return "/broderjobs/estudiante/empresa-detalle/"+id+"/#resultado-evaluacion"
        else:
            return reverse_lazy('estudiante-empresa-lista')

class EmpresaListaView(LoginRequiredMixin, TemplateView):

    template_name = 'estudiante/empresa-lista.html'

class EmpresaBusquedaView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        busqueda = request.GET['busqueda']
        empresas = Empresa.objects.filter(Q(nombre__icontains=busqueda))
        a_empresas =[]
        for i in range(0, len(empresas)):
            ranking = RankingEmpresa()
            try:
                ranking = RankingEmpresa.objects.get(empresa=empresas[i].id)
            except RankingEmpresa.DoesNotExist:
                ranking = None
            if ranking is not None:
                ranking_general = str(round(float(ranking.ranking_general), 1))
            else:
                ranking_general = "0.0"
            sector = empresas[i].nombre
            if empresas[i].sector is not None:
                sector = Sector.objects.get(id=empresas[i].sector.id).descripcion
            e = {
                "id": empresas[i].id,
                "nombre": empresas[i].nombre,
                "logo": empresas[i].set_logo,
                "sector": sector,
                "ranking_general": ranking_general,
            }
            a_empresas.append(e)
        # data = serializers.serialize('json', a_empresas,
        #                              fields=('id','nombre', 'sector', 'logo', 'ranking_general' ))
        data = json.dumps(a_empresas)
        return HttpResponse(data, content_type='application/json')

class OportunidadesEmpresaView(TemplateView):
    template_name = 'estudiante/oportunidades-empresa.html'
    def get_context_data(self, **kwargs):
        id = kwargs.get('id', None)
        empresa = get_object_or_404(Empresa, pk=id)
        oportunidades =  Oportunidad.objects.filter(empresa_id = empresa.id, estado_oportunidad = 'A').order_by("fecha_publicacion")
        context = super(OportunidadesEmpresaView, self).get_context_data(**kwargs)
        context['empresa'] = empresa
        context['oportunidades'] = oportunidades
        return context

class MiCVView(LoginRequiredMixin, FormView):

    form_class = forms.FotoForm
    template_name = 'estudiante/mi-cv.html'
    success_url = reverse_lazy('mi-cv')

    def get_context_data(self, **kwargs):
        user = self.request.user
        persona = get_object_or_404(Persona, usuario_id=user.id)
        estudiante = get_object_or_404(Estudiante, persona_id=persona.id)
        context = super(MiCVView, self).get_context_data(**kwargs)
        if persona.fecha_nacimiento is not None:
            edad = utils.calular_edad(persona.fecha_nacimiento)
            context['edad'] = edad
        context['usuario'] = user
        context['persona'] = persona
        context['estudiante'] = estudiante
        context['resumen'] = Resumen.objects.get(estudiante_id=estudiante.id)
        context['actividades_extra'] = ActividadesExtra.objects.filter(estudiante_id=estudiante.id)
        context['experiencias_profesionales'] = ExperienciaProfesional.objects.filter(estudiante_id=estudiante.id)
        context['voluntariados'] = Voluntariado.objects.filter(estudiante_id=estudiante.id)
        return context

    def form_valid(self, form):
        try:
            foto = self.request.FILES['foto']
        except:
            foto = None
        user = self.request.user
        persona = Persona.objects.get(usuario_id=user.id)
        estudiante = Estudiante.objects.get(persona_id=persona.id)
        if foto is not None:
            estudiante.foto = foto
        else:
            estudiante.foto.delete()
        estudiante.save()
        return super(MiCVView, self).form_valid(form)

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

class FotoView(LoginRequiredMixin, SuccessMessageMixin, FormView):
    form_class = forms.FotoForm
    template_name = 'estudiante/mi-cv-foto.html'
    success_url =reverse_lazy('mi-cv')

    # def get_object(self, queryset=None):
    #     user = self.request.user
    #     persona = Persona.objects.get(usuario_id=user.id)
    #     estudiante = Estudiante.objects.get(persona_id =persona.id)
    #     return estudiante

    def post(self, request, *args, **kwargs):

        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if request.is_ajax():
            foto = self.request.FILES['foto']
            user = self.request.user
            persona = Persona.objects.get(usuario_id=user.id)
            estudiante = Estudiante.objects.get(persona_id=persona.id)
            estudiante.foto = foto
            estudiante.save()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form, **kwargs)

    def form_valid(self, form):
        foto = self.request.FILES['foto']
        user = self.request.user
        persona = Persona.objects.get(usuario_id=user.id)
        estudiante = Estudiante.objects.get(persona_id=persona.id)
        estudiante.foto = self.request.FILES['foto']
        estudiante.save()
        return super(FotoView, self).form_valid(form)

class InfoPersonalView(LoginRequiredMixin, FormView):
    form_class =forms.InfoPersonalForm
    template_name = 'estudiante/mi-cv-info-personal.html'
    success_url = reverse_lazy('mi-cv')

    def get_initial(self):
        user = self.request.user
        usuario = User.objects.get(pk = user.id)
        persona = Persona.objects.get(usuario_id=user.id)
        estudiante = Estudiante.objects.get(persona_id =persona.id)
        universidad = estudiante.universidad
        universidad_hidden = universidad.id
        carrera = estudiante.carrera
        carrera_hidden = carrera.id
        pais = estudiante.pais
        pais_hidden = pais.id
        ciudad = estudiante.ciudad
        ciudad_hidden = ciudad.id
        return {
            'email': usuario.email,
            'telefono': persona.telefono,
            'fecha_nacimiento': persona.fecha_nacimiento,
            'universidades': universidad,
            'universidades_hidden': universidad_hidden,
            'carreras': carrera,
            'carreras_hidden': carrera_hidden,
            'paises': pais,
            'paises_hidden': pais_hidden,
            'ciudades': ciudad,
            'ciudades_hidden': ciudad_hidden,
            'grado_estudio': estudiante.grado_estudio,
            'ano_graduacion': estudiante.ano_graduacion,
            'semestre_graduacion': estudiante.semestre_graduacion,
            'semestre_inicio_estudio': estudiante.semestre_inicio_estudio,
            'ano_inicio_estudio': estudiante.ano_inicio_estudio}

    def form_invalid(self, form):
        # response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():

            return JsonResponse(form.errors, status=400)
        else:
            return ''
            # return response

    def form_valid(self, form):
        user = self.request.user
        usuario = User.objects.get(pk = user.id)
        persona = Persona.objects.get(usuario_id=user.id)
        grado_estudio = form.cleaned_data['grado_estudio']
        id_universidad = form.cleaned_data['universidades_hidden']
        id_carrera = form.cleaned_data['carreras_hidden']
        id_pais = form.cleaned_data['paises_hidden']
        id_ciudad = form.cleaned_data['ciudades_hidden']
        ano_inicio = form.cleaned_data['ano_inicio_estudio']
        semestre_inicio = form.cleaned_data['semestre_inicio_estudio']
        ano_graduacion = form.cleaned_data['ano_graduacion']
        semestre_graduacion = form.cleaned_data['semestre_graduacion']

        estudiante = Estudiante.objects.get(persona_id=persona.id)
        estudiante.grado_estudio = grado_estudio
        universidad = Universidad.objects.get(id= id_universidad )
        if universidad is not None:
            estudiante.universidad = universidad
        carrera = Carrera.objects.get(id = id_carrera)
        if carrera is not None:
            estudiante.carrera = carrera
        pais = Pais.objects.get(id= id_pais)
        if pais is not None:
            estudiante.pais = pais
        ciudad = Ciudad.objects.get(id = id_ciudad)
        if ciudad is not None:
            estudiante.ciudad = ciudad

        # estudiante.universidad = universidad
        # estudiante.carrera = carrera
        # estudiante.pais = pais
        # estudiante.ciudad = ciudad
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

class ResumenView(LoginRequiredMixin, FormView):
    template_name = 'estudiante/mi-cv-resumen.html'
    form_class = forms.ResumenForm
    success_url = reverse_lazy('mi-cv')
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

class DisponibilidadView(LoginRequiredMixin, SuccessMessageMixin, AjaxTemplateMixin, UpdateView):
    template_name = 'estudiante/mi-cv-disponibilidad.html'
    form_class = forms.DisponibilidadForm
    success_url = reverse_lazy('mi-cv')

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

class IdiomaView(LoginRequiredMixin, FormView):
    template_name = 'estudiante/mi-cv-idioma.html'
    form_class = forms.IdiomaForm
    success_url = reverse_lazy('mi-cv')

    def get_initial(self):
        user = self.request.user
        persona = Persona.objects.get(usuario_id=user.id)
        estudiante = Estudiante.objects.get(persona_id=persona.id)

        return {'idioma': estudiante.idioma.all()}

    def form_valid(self, form):
        user = self.request.user
        persona = Persona.objects.get(usuario_id=user.id)
        estudiante = Estudiante.objects.get(persona_id=persona.id)
        estudiante.idioma = form.cleaned_data['idioma']
        estudiante.save()
        return super(IdiomaView, self).form_valid(form)

class ConocimientoView(LoginRequiredMixin, FormView):
    template_name = 'estudiante/mi-cv-conocimiento.html'
    form_class = forms.ConocimientoForm
    success_url = reverse_lazy('mi-cv')

    def get_initial(self):
        user = self.request.user
        persona = Persona.objects.get(usuario_id=user.id)
        estudiante = Estudiante.objects.get(persona_id=persona.id)

        return {'conocimiento': estudiante.conocimiento.all()}

    def get_object(self, queryset=None):
        user = self.request.user
        persona = Persona.objects.get(usuario_id=user.id)
        estudiante = Estudiante.objects.get(persona_id =persona.id)
        return estudiante

    def form_valid(self, form):
        con = form.cleaned_data['conocimiento']
        user = self.request.user
        persona = Persona.objects.get(usuario_id=user.id)
        estudiante = Estudiante.objects.get(persona_id=persona.id)
        estudiante.conocimiento = form.cleaned_data['conocimiento']
        estudiante.save()
        return super(ConocimientoView, self).form_valid(form)

class ActividadExtraView(LoginRequiredMixin, SuccessMessageMixin, AjaxTemplateMixin,UpdateView):
    form_class = forms.ActividadesExtraForm
    template_name = 'estudiante/mi-cv-actividad-extra.html'
    success_url = reverse_lazy('mi-cv')

    def get_object(self, queryset=None):
        id = self.kwargs["id"]
        actividad_extra = ActividadesExtra.objects.get(id =id)
        return actividad_extra

class ActividadExtraCrearView(LoginRequiredMixin, SuccessMessageMixin, AjaxTemplateMixin,FormView):
    form_class = forms.ActividadesExtraForm
    template_name = 'estudiante/mi-cv-actividad-extra.html'
    success_url = reverse_lazy('mi-cv')

    def form_valid(self, form):
        user = self.request.user
        persona = Persona.objects.get(usuario_id=user.id)
        estudiante = Estudiante.objects.get(persona_id=persona.id)
        actividad_extra = ActividadesExtra()
        organizacion = form.cleaned_data['organizacion']
        descripcion = form.cleaned_data['descripcion']
        actividad_extra.estudiante = estudiante
        actividad_extra.organizacion = organizacion
        actividad_extra.descripcion = descripcion
        actividad_extra.save()
        return super(ActividadExtraCrearView, self).form_valid(form)

class ActividadExtraEliminarView(LoginRequiredMixin, SuccessMessageMixin, AjaxTemplateMixin, DeleteView):

   template_name = 'estudiante/mi-cv-actividad-extra-eliminar.html'
   model = ActividadesExtra
   success_url = reverse_lazy('mi-cv')

class ExperienciaView(LoginRequiredMixin, SuccessMessageMixin, AjaxTemplateMixin,FormView):
    template_name = 'estudiante/mi-cv-experiencia.html'
    form_class = forms.ExperienciaForm
    success_url = reverse_lazy('mi-cv')

    def get_initial(self):
        id = self.kwargs["id"]
        experiencia = get_object_or_404(ExperienciaProfesional, id= id)
        puestos = experiencia.puesto
        puestos_hidden = experiencia.puesto.id

        if experiencia.empresa is None:
            empresas = experiencia.empresa_referencial
            empresas_hidden = None
        else:
            empresas = experiencia.empresa
            empresas_hidden = experiencia.empresa.id
        descripcion = experiencia.descripcion
        fecha_desde = experiencia.fecha_desde
        fecha_hasta = experiencia.fecha_hasta
        return {'puestos': puestos, 'puestos_hidden': puestos_hidden,
                'empresas': empresas, 'empresas_hidden': empresas_hidden,
                'fecha_desde': fecha_desde, 'fecha_hasta': fecha_hasta,
                'descripcion': descripcion}

    def form_valid(self, form):
        id = self.kwargs["id"]
        user = self.request.user
        persona = Persona.objects.get(usuario_id=user.id)
        estudiante = Estudiante.objects.get(persona_id=persona.id)
        experiencia = ExperienciaProfesional.objects.get(id = id )
        puesto_descripcion = form.cleaned_data['puestos']
        empresa_descripcion = form.cleaned_data['empresas']
        puesto_id = form.cleaned_data['puestos_hidden']
        empresa_id = form.cleaned_data['empresas_hidden']

        fecha_desde = form.cleaned_data['fecha_desde']
        fecha_hasta = form.cleaned_data['fecha_hasta']
        descripcion = form.cleaned_data['descripcion']
        experiencia.estudiante = estudiante
        puesto = Puesto.objects.get(id=puesto_id)
        if empresa_id != "0":
            empresa = Empresa.objects.get(id=empresa_id)
            experiencia.empresa = empresa
        else:
            experiencia.empresa = None
            experiencia.empresa_referencial = empresa_descripcion
        experiencia.puesto = puesto
        if fecha_desde is not None:
            experiencia.fecha_desde = fecha_desde
        if fecha_hasta is not None:
            experiencia.fecha_hasta = fecha_hasta
            experiencia.trabajo_actual = 'N'
        else:
            experiencia.trabajo_actual = 'S'
        experiencia.descripcion = descripcion
        experiencia.save()
        return super(ExperienciaView, self).form_valid(form)

class ExperienciaCrearView(LoginRequiredMixin, SuccessMessageMixin, AjaxTemplateMixin,FormView):
    form_class = forms.ExperienciaForm
    template_name = 'estudiante/mi-cv-experiencia.html'
    success_url = reverse_lazy('mi-cv')

    def form_invalid(self, form):
        # response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            # return response
            return ''

    def form_valid(self, form):
        user = self.request.user
        usuario = User.objects.get(pk = user.id)
        persona = Persona.objects.get(usuario_id=user.id)
        estudiante = Estudiante.objects.get(persona_id=persona.id)
        experiencia = ExperienciaProfesional()
        puesto_descripcion = form.cleaned_data['puestos']
        empresa_descripcion = form.cleaned_data['empresas']
        puesto_id = form.cleaned_data['puestos_hidden']
        empresa_id = form.cleaned_data['empresas_hidden']

        fecha_desde = form.cleaned_data['fecha_desde']
        fecha_hasta = form.cleaned_data['fecha_hasta']
        descripcion = form.cleaned_data['descripcion']
        experiencia.estudiante = estudiante
        puesto = Puesto.objects.get(id=puesto_id)
        if empresa_id != "0":
            empresa = Empresa.objects.get(id=empresa_id)
            experiencia.empresa = empresa
        else:
            experiencia.empresa_referencial = empresa_descripcion
        experiencia.puesto = puesto
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

class ExperienciaEliminarView(LoginRequiredMixin, SuccessMessageMixin, AjaxTemplateMixin, DeleteView):
    template_name = 'estudiante/mi-cv-experiencia-eliminar.html'
    model = ExperienciaProfesional
    success_url = reverse_lazy('mi-cv')

class VoluntariadoView(LoginRequiredMixin, SuccessMessageMixin, AjaxTemplateMixin,UpdateView):
    form_class = forms.VoluntariadoForm
    template_name = 'estudiante/mi-cv-voluntariado.html'
    success_url = reverse_lazy('mi-cv')

    def get_object(self, queryset=None):
        id = self.kwargs["id"]
        voluntariado = Voluntariado.objects.get(id =id)
        return voluntariado

class VoluntariadoCrearView(LoginRequiredMixin, SuccessMessageMixin, AjaxTemplateMixin,FormView):
    form_class = forms.VoluntariadoForm
    template_name = 'estudiante/mi-cv-voluntariado.html'
    success_url = reverse_lazy('mi-cv')

    def form_valid(self, form):
        user = self.request.user
        usuario = User.objects.get(pk = user.id)
        persona = Persona.objects.get(usuario_id=user.id)
        estudiante = Estudiante.objects.get(persona_id=persona.id)
        voluntariado = Voluntariado()
        cargo = form.cleaned_data['cargo']
        organizacion = form.cleaned_data['organizacion']
        fecha_desde = form.cleaned_data['fecha_desde']
        fecha_hasta = form.cleaned_data['fecha_hasta']
        descripcion = form.cleaned_data['descripcion']
        voluntariado.estudiante = estudiante
        voluntariado.cargo = cargo
        voluntariado.organizacion = organizacion
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

class VoluntariadoEliminarView(LoginRequiredMixin, SuccessMessageMixin, AjaxTemplateMixin, DeleteView):

   template_name = 'estudiante/mi-cv-voluntariado-eliminar.html'
   model = Voluntariado
   success_url = reverse_lazy('mi-cv')

class UniversidadBusquedaView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        busqueda = request.GET['busqueda']
        universidades = Universidad.objects.filter(Q(descripcion__icontains=busqueda))
        data = serializers.serialize('json', universidades,
                                     fields=('id','descripcion'))
        return HttpResponse(data, content_type='application/json')

class CarreraBusquedaView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        busqueda = request.GET['busqueda']
        carreras = Carrera.objects.filter(Q(descripcion__icontains=busqueda))
        data = serializers.serialize('json', carreras,
                                     fields=('id','descripcion'))
        return HttpResponse(data, content_type='application/json')

class EstudianteEmpresaBusquedaView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        busqueda = request.GET['busqueda']
        empresas = Empresa.objects.filter(Q(nombre__icontains=busqueda))
        data = serializers.serialize('json', empresas,
                                     fields=('id','nombre'))
        return HttpResponse(data, content_type='application/json')

class EstudiantePuestoBusquedaView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        busqueda = request.GET['busqueda']
        puestos = Puesto.objects.filter(Q(descripcion__icontains=busqueda))
        data = serializers.serialize('json', puestos,
                                     fields=('id','descripcion'))
        return HttpResponse(data, content_type='application/json')

class OportunidadDetalleView(LoginRequiredMixin, TemplateView):
    login_required = True
    template_name = 'estudiante/oportunidad-detalle.html'
    def get_context_data(self, **kwargs):
        id = kwargs.get('id', None)
        user = self.request.user
        usuario = User.objects.get(pk = user.id)
        persona = Persona.objects.get(usuario_id=user.id)
        estudiante = Estudiante.objects.get(persona_id=persona.id)

        oportunidad =  get_object_or_404(Oportunidad, pk=id)
        empresa = get_object_or_404(Empresa, pk=oportunidad.empresa.id)
        postulacion = Postulacion()
        try:
            postulacion = Postulacion.objects.get(oportunidad_id = oportunidad.id, estudiante_id = estudiante.id)
        except Postulacion.DoesNotExist:
            postulacion = None
        context = super(OportunidadDetalleView, self).get_context_data(**kwargs)
        context['empresa'] = empresa
        context['oportunidad'] = oportunidad
        context['postulacion'] = postulacion
        return context

class OportunidadBusquedaView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        busqueda = request.GET['busqueda']
        oportunidades = Oportunidad.objects.filter(
            Q(titulo__icontains=busqueda) | Q(empresa__nombre__icontains = busqueda) |
            Q(ciudad__descripcion__icontains=busqueda) | Q(pais__descripcion__icontains = busqueda) |
            Q(tipo_puesto__descripcion__startswith=busqueda) | Q(carga_horaria__descripcion__startswith=busqueda) |
            Q(carrera__descripcion__startswith=busqueda) | Q(conocimiento__descripcion__startswith=busqueda),
            estado_oportunidad = 'A'
        ).order_by('fecha_publicacion').distinct()
        a_oportunidades =[]
        for i in range(0, len(oportunidades)):
            empresa = Empresa.objects.get(id=oportunidades[i].empresa.id)
            ciudad = empresa.ciudad
            pais = empresa.pais
            if oportunidades[i].remuneracion is None or  oportunidades[i].remuneracion == 'No especificado' :
                remuneracion = 'No Especificado'
            else:
                remuneracion = str(oportunidades[i].remuneracion_min)+ ' - ' + str(oportunidades[i].remuneracion_max)
            e = {
                "id": oportunidades[i].id,
                "titulo": oportunidades[i].titulo,
                "empresa": empresa.nombre,
                "logo": empresa.set_logo,
                "ubicacion": str(ciudad) + ', ' +str(pais),
                "fecha_cese": str(oportunidades[i].fecha_cese),
                "remuneracion": remuneracion,
            }
            a_oportunidades.append(e)
        # data = serializers.serialize('json', a_empresas,
        #                              fields=('id','nombre', 'sector', 'logo', 'ranking_general' ))
        data = json.dumps(a_oportunidades)
        return HttpResponse(data, content_type='application/json')

class OportunidadPostularView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        id = request.GET['id']
        persona = get_object_or_404(Persona, usuario_id = request.user.id)
        estudiante =  get_object_or_404(Estudiante, persona_id = persona.id)
        data =[]
        p, created = Postulacion.objects.get_or_create(oportunidad_id = id, estudiante_id = estudiante.id)
        if created is True:
            p.fecha_creacion = date.today()
            p.estado = 'A'
            p.estado_postulacion = 'P'
            p.save()
            data.append(('CANCELAR'))
        else:
            estado = p.estado
            if estado == 'A':
                p.estado = 'I'
                p.estado_postulacion = ''
                data.append(('POSTULAR'))
            else:
                p.estado = 'A'
                p.estado_postulacion = 'P'
                data.append(('CANCELAR'))
            p.fecha_creacion = date.today()
            p.save()
        data_json = json.dumps(data)
        return HttpResponse(data_json, content_type='application/json')

class ProcesoListaView(LoginRequiredMixin, TemplateView):
    login_required = True
    template_name = 'estudiante/proceso-listar.html'
    def get_context_data(self, **kwargs):
        user = self.request.user
        persona = get_object_or_404(Persona, usuario_id = user.id)
        estudiante =  get_object_or_404(Estudiante, persona_id = persona.id)
        p = Postulacion.objects.filter(estudiante_id = estudiante.id, estado = 'A').order_by('fecha_creacion')

        postulaciones =[]
        for i in range(0, len(p)):
            oportunidad = get_object_or_404(Oportunidad, id = p[i].oportunidad.id)
            empresa = Empresa.objects.get(id=oportunidad.empresa.id)
            ciudad = empresa.ciudad
            pais = empresa.pais
            estado_postulacion = 'Postulado'
            if p[i].estado_postulacion == 'E':
                estado_postulacion = 'En Evaluacion'
            if p[i].estado_postulacion == 'F':
                estado_postulacion = 'Finalizado'
            remuneracion = oportunidad.remuneracion
            e = {
                "id": p[i].id,
                "id_oportunidad": oportunidad.id,
                "titulo": oportunidad.titulo,
                "empresa": empresa.nombre,
                "logo": empresa.set_logo,
                "ubicacion": str(ciudad) + ', ' +str(pais),
                "fecha_cese": str(oportunidad.fecha_cese),
                "remuneracion": remuneracion,
                "estado_postulacion": estado_postulacion,
            }
            postulaciones.append(e)
        # data = serializers.serialize('json', a_empresas,
        #                              fields=('id','nombre', 'sector', 'logo', 'ranking_general' ))
        context = super(ProcesoListaView, self).get_context_data(**kwargs)
        context['postulaciones'] = postulaciones
        return context

class ProcesoDetalleView(LoginRequiredMixin, TemplateView):
    login_required = True
    template_name = 'estudiante/proceso-detalle.html'
    def get_context_data(self, **kwargs):
        id = kwargs.get('id', None)
        postulacion =  get_object_or_404(Postulacion, pk=id)
        oportunidad =  get_object_or_404(Oportunidad, pk = postulacion.oportunidad.id)
        empresa = get_object_or_404(Empresa, pk=oportunidad.empresa.id)
        try:
            mensajes = Mensaje_Destinatario.objects.filter(usuario_destinatario_id=self.request.user, mensaje__postulacion_id = postulacion.id)
        except mensajes.DoesNotExist:
            mensajes = None
        context = super(ProcesoDetalleView, self).get_context_data(**kwargs)
        context['postulacion'] = postulacion
        context['oportunidad'] = oportunidad
        context['empresa'] = empresa
        context['mensajes'] = mensajes
        return context