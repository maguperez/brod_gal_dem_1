from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin
from . import forms
from django.views.generic import TemplateView, FormView
from django.core.urlresolvers import reverse_lazy
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.generic import UpdateView, CreateView
from django.views.generic import TemplateView, FormView
from django.core.urlresolvers import reverse_lazy
from .models import Oportunidad, Postulacion
from estudiante.models import Estudiante
from models import Persona, GradoEstudio, Universidad, Carrera, Pais, Ciudad, TipoPuesto, Idioma, CargaHoraria, TipoRemuneracion, Beneficio, Conocimiento
from empresa.models import Representante, Empresa
from django.db.models import Q, CharField
from oportunidad  import utils
import json
from cStringIO import StringIO


# Create your views here.
class OportunidadCrearView(FormView):
    form_class = forms.OportunidadForm
    template_name = 'oportunidad/crear.html'
    success_url = reverse_lazy('empresa-oportunidad-listar')

    def form_valid(self, form):
        user = self.request.user
        persona = get_object_or_404(Persona, usuario_id=user.id)
        representante =get_object_or_404(Representante, persona_id=persona.id)
        empresa = get_object_or_404(Empresa, id=representante.empresa.id)
        titulo = form.cleaned_data['titulo']
        carga_horaria = form.cleaned_data['carga_horaria']
        pais = form.cleaned_data['pais']
        id_ciudad = form.cleaned_data['ciudad_hidden']

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
        print("ciudad")
        print(id_ciudad)
        if id_ciudad is not None and id_ciudad != '':
            try:
                ciudad = Ciudad.objects.get(id = id_ciudad)
            except Ciudad.DoesNotExist:
                ciudad = None
            if ciudad is not None:
                oportunidad.ciudad = ciudad
        oportunidad.remuneracion = remuneracion
        if fecha_cese is not None:
            oportunidad.fecha_cese = fecha_cese
        oportunidad.tipo_puesto = tipo_puesto
        oportunidad.grado_estudio = grado_estudio
        oportunidad.resumen = resumen
        oportunidad.estado = 'A'
        oportunidad.save()

        oportunidad.universidad = universidad
        oportunidad.carrera = carrera
        oportunidad.idioma = idioma
        oportunidad.conocimiento = conocimiento

        oportunidad.beneficio = beneficio
        if '_guardar' in self.request.POST:
            oportunidad.estado_oportunidad = 'P'
        elif '_anunciar' in self.request.POST:
            oportunidad.estado_oportunidad = 'A'

        oportunidad.save()
        return super(OportunidadCrearView, self).form_valid(form)

    def form_invalid(self, form):
        response = super(OportunidadCrearView, self).form_invalid(form)
        return response

class OportunidadEditarView(UpdateView):
    form_class = forms.OportunidadForm
    template_name = 'oportunidad/editar.html'
    success_url = reverse_lazy('empresa-oportunidad-listar')

    def get_initial(self):
        id = self.kwargs["id"]
        oportunidad =get_object_or_404(Oportunidad, id = id)
        return {'pais': oportunidad.pais, 'ciudad_hidden': oportunidad.ciudad.id}

    def get_object(self, queryset=None):
        id = self.kwargs["id"]
        oportunidad =get_object_or_404(Oportunidad, id = id)

        return oportunidad

    def form_valid(self, form):
        estado =  form.cleaned_data['estado_oportunidad']
        titulo = form.cleaned_data['titulo']
        carga_horaria = form.cleaned_data['carga_horaria']
        pais = form.cleaned_data['pais']
        id_ciudad = form.cleaned_data['ciudad_hidden']

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
        id = self.kwargs["id"]
        oportunidad =get_object_or_404(Oportunidad, id = id)

        oportunidad.estado_oportunidad = estado
        oportunidad.estado = 'A'
        oportunidad.titulo = titulo
        oportunidad.carga_horaria  = carga_horaria
        oportunidad.pais = pais
        if id_ciudad is not None and id_ciudad != '':
            try:
                ciudad = Ciudad.objects.get(id = id_ciudad)
            except Ciudad.DoesNotExist:
                ciudad = None
            if ciudad is not None:
                oportunidad.ciudad = ciudad
        else:
            oportunidad.ciudad = None
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

class OportunidadView(TemplateView):
    login_required = True
    template_name = 'oportunidad/ver.html'
    def get_context_data(self, **kwargs):
        id = kwargs.get('id', None)
        oportunidad =  get_object_or_404(Oportunidad, pk=id)
        empresa = get_object_or_404(Empresa, pk=oportunidad.empresa.id)
        context = super(OportunidadView, self).get_context_data(**kwargs)
        context['empresa'] = empresa
        context['oportunidad'] = oportunidad
        return context

def datatable_candidatos(request):
    id = request.GET['id']
    objects = Postulacion.objects.filter(oportunidad_id = id)

    list_display = ['semestre_inicio_estudio', 'ano_inicio_estudio', 'semestre_graduacion']
    list_filter = [f.name for f in Estudiante._meta.fields if isinstance(f, CharField)]
    #a simple way to bring all CharFields, can be defined in specifics
    list_filter = [f.name for f in Estudiante._meta.fields]

    # count total items:
    iTotalRecords = objects.count()

    # # #filter on list_filter using __contains
    # search = request.GET['sSearch']
    # queries = [Q(**{f+'__contains' : search}) for f in list_filter]
    # qs = reduce(lambda x, y: x|y, queries)
    # objects = objects.filter(qs)

    # #sorting
    # order = dict( enumerate(list_display) )
    # dirs = {'asc': '', 'desc': '-'}
    # ordering = dirs[request.GET['sSortDir_0']] + order[int(request.GET['iSortCol_0'])]
    # objects = objects.order_by(ordering)
    #
    # count items after filtering:
    iTotalDisplayRecords = objects.count()


    # finally, slice according to length sent by dataTables:
    start = int(request.GET['start'])
    length = int(request.GET['length'])
    objects = objects[ start : (start+length)]

    # extract information
    data1 = utils.obtener_candidatos(objects)
    # data = [map(lambda field: getattr(obj, field), list_display) for obj in objects]

    #define response
    response = {
        'aaData': data1,
        'iTotalRecords': iTotalRecords,
        'iTotalDisplayRecords': iTotalDisplayRecords,
        'draw': request.GET['draw']
    }

    #serialize to json
    s = StringIO()
    json.dump(response, s)
    s.seek(0)
    return HttpResponse(s.read())

def siguiente_fase( request ):
    id = request.GET['id']
    fase = request.GET['fase']
    #define response
    response = {
        'aaData': ''

    }
    #serialize to json
    s = StringIO()
    json.dump(response, s)
    s.seek(0)
    return HttpResponse(s.read())