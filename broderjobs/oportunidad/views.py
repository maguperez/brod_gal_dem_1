# coding=utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin
from . import forms, utils
from django.views.generic import TemplateView, FormView
from django.core.urlresolvers import reverse_lazy
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.generic import UpdateView, CreateView
from django.views.generic import TemplateView, FormView
from django.core.urlresolvers import reverse_lazy
from broderjobs import constants
from .models import Oportunidad, Postulacion, ProcesoFase
from estudiante.models import Estudiante
from models import Persona, GradoEstudio, Universidad, Carrera, Pais, Ciudad, TipoPuesto, Idioma, CargaHoraria, TipoRemuneracion, Beneficio, Conocimiento
from empresa.models import Representante, Empresa
from mensaje.models import Mensaje, Mensaje_Destinatario
from mensaje.utils import enviar_mensaje_multiple_estudiantes, enviar_notificacion_multiple_estudiantes
from django.db.models import Q, CharField
from datetime import date, datetime
import json
from cStringIO import StringIO



# Create your views here.
class OportunidadCrearView(FormView):
    form_class = forms.OportunidadForm
    template_name = 'oportunidad/crear.html'
    success_url = reverse_lazy('empresa-oportunidad-listar')

    def get_initial(self):
        user = self.request.user
        persona = Persona.objects.get(usuario_id=user.id)
        representante = Representante.objects.get(persona_id =persona.id)
        empresa = Empresa.objects.get(id=representante.empresa.id)
        return {'longitud': empresa.longitud, 'latitud': empresa.latitud}

    def form_valid(self, form):
        user_id = self.request.user
        user = get_object_or_404(User, pk = user_id.id)
        persona = get_object_or_404(Persona, usuario_id=user.id)
        representante =get_object_or_404(Representante, persona_id=persona.id)
        empresa = get_object_or_404(Empresa, id=representante.empresa.id)
        fase = fase =  get_object_or_404(ProcesoFase, pk = 1)
        titulo = form.cleaned_data['titulo']
        carga_horaria = form.cleaned_data['carga_horaria']
        pais = form.cleaned_data['pais']
        id_ciudad = form.cleaned_data['ciudad_hidden']

        remuneracion = form.cleaned_data['remuneracion']

        if remuneracion is not None:
            if remuneracion.id is 1:
                remuneracion_min = None
                remuneracion_max = None
            elif remuneracion.id is 2:
                remuneracion_min = form.cleaned_data['remuneracion_min']
                remuneracion_max = form.cleaned_data['remuneracion_max']
            elif remuneracion.id is 3:
                remuneracion_min = form.cleaned_data['remuneracion_min']
                remuneracion_max = None

        fecha_cese = form.cleaned_data['fecha_cese']
        resumen = form.cleaned_data['resumen']
        beneficio = form.cleaned_data['beneficio']
        tipo_puesto = form.cleaned_data['tipo_puesto']

        grado_estudio = form.cleaned_data['grado_estudio']
        universidad = form.cleaned_data['universidad']
        carrera = form.cleaned_data['carrera']
        idioma = form.cleaned_data['idioma']
        conocimiento = form.cleaned_data['conocimiento']
        longitud = form.cleaned_data['longitud']
        latitud = form.cleaned_data['latitud']

        oportunidad = Oportunidad()
        oportunidad.empresa = empresa
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

        oportunidad.remuneracion = remuneracion
        oportunidad.remuneracion_min = remuneracion_min
        oportunidad.remuneracion_max = remuneracion_max

        if fecha_cese is not None:
            oportunidad.fecha_cese = fecha_cese
        oportunidad.tipo_puesto = tipo_puesto

        oportunidad.resumen = resumen
        oportunidad.estado = constants.estado_activo
        oportunidad.fase = fase
        if '_guardar' in self.request.POST:
            oportunidad.estado_oportunidad = constants.estado_archivado
        elif '_anunciar' in self.request.POST:
            oportunidad.estado_oportunidad = constants.estado_abierto
            oportunidad.fecha_publicacion = datetime.now()
        oportunidad.longitud = longitud
        oportunidad.latitud = latitud
        oportunidad.usuario_creacion = str(user.username)
        oportunidad.usuario_modificacion = str(user.username)
        oportunidad.fecha_creacion = datetime.now()
        oportunidad.fecha_modificacion = datetime.now()
        oportunidad.save()

        oportunidad.universidad = universidad
        oportunidad.carrera = carrera
        oportunidad.idioma = idioma
        oportunidad.conocimiento = conocimiento
        oportunidad.beneficio = beneficio
        oportunidad.grado_estudio = grado_estudio
        oportunidad.save()
        return super(OportunidadCrearView, self).form_valid(form)

    def form_invalid(self, form):
        response = super(OportunidadCrearView, self).form_invalid(form)
        return response

class OportunidadEditarView(FormView):
    form_class = forms.OportunidadForm
    template_name = 'oportunidad/editar.html'
    success_url = reverse_lazy('empresa-oportunidad-listar')

    def get_initial(self):
        id = self.kwargs["id"]
        oportunidad =get_object_or_404(Oportunidad, id = id)
        if oportunidad.ciudad is not None:
            ciudad_id = oportunidad.ciudad.id
        else:
            ciudad_id = '0'
        return {'titulo': oportunidad.titulo,
                'carga_horaria': oportunidad.carga_horaria,
                'remuneracion': oportunidad.remuneracion,
                'remuneracion_min' : oportunidad.remuneracion_min,
                'remuneracion_max' : oportunidad.remuneracion_max,
                'fecha_cese': oportunidad.fecha_cese,
                'beneficio': oportunidad.beneficio,
                'resumen': oportunidad.resumen,
                'carga_horaria': oportunidad.carga_horaria,
                'tipo_puesto': oportunidad.tipo_puesto,
                'estado': oportunidad.estado,
                'estado_oportunidad': oportunidad.estado_oportunidad,
                'grado_estudio': oportunidad.grado_estudio.all(),
                'universidad': oportunidad.universidad.all(),
                'carrera': oportunidad.carrera.all(),
                'idioma': oportunidad.idioma.all(),
                'conocimiento': oportunidad.conocimiento.all(),
                'beneficio': oportunidad.beneficio.all(),
                'longitud': oportunidad.longitud,
                'latitud': oportunidad.latitud,
                'pais': oportunidad.pais, 'ciudad_hidden': ciudad_id}

    def get_context_data(self, **kwargs):
        id = self.kwargs["id"]
        oportunidad =get_object_or_404(Oportunidad, id = id)
        context = super(OportunidadEditarView, self).get_context_data(**kwargs)
        context['oportunidad'] = oportunidad
        return context

    def get_object(self, queryset=None):
        id = self.kwargs["id"]
        oportunidad =get_object_or_404(Oportunidad, id = id)
        return oportunidad

    def form_valid(self, form):
        user = get_object_or_404(User, pk = self.request.user.id)
        fase_postulacion = fase =  get_object_or_404(ProcesoFase, pk = 1)
        titulo = form.cleaned_data['titulo']
        carga_horaria = form.cleaned_data['carga_horaria']
        pais = form.cleaned_data['pais']
        id_ciudad = form.cleaned_data['ciudad_hidden']

        remuneracion = form.cleaned_data['remuneracion']

        if remuneracion is not None:
            if remuneracion.id is 1:
                remuneracion_min = None
                remuneracion_max = None
            elif remuneracion.id is 2:
                remuneracion_min = form.cleaned_data['remuneracion_min']
                remuneracion_max = form.cleaned_data['remuneracion_max']
            elif remuneracion.id is 3:
                remuneracion_min = form.cleaned_data['remuneracion_min']
                remuneracion_max = None



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
        oportunidad = get_object_or_404(Oportunidad, id = id)

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
        oportunidad.remuneracion_min = remuneracion_min
        oportunidad.remuneracion_max = remuneracion_max

        if fecha_cese is not None:
            oportunidad.fecha_cese = fecha_cese
        oportunidad.resumen = resumen
        oportunidad.tipo_puesto = tipo_puesto

        oportunidad.estado = constants.estado_activo
        estado_anterior = oportunidad.estado_oportunidad

        if '_guardar' in self.request.POST:
            if oportunidad.fecha_cese is not None and date.today() > oportunidad.fecha_cese:
                estado_nuevo = constants.estado_cerrado
            else:
                estado_nuevo = constants.estado_abierto
                oportunidad.fecha_publicacion = datetime.now()

        elif '_archivar' in self.request.POST:
            estado_nuevo = constants.estado_archivado

        elif '_abrir' in self.request.POST:
            estado_nuevo = constants.estado_abierto
            oportunidad.pk = None
            oportunidad.fase = fase_postulacion
            oportunidad.fecha_publicacion = datetime.now()

        if estado_anterior == constants.estado_abierto and estado_nuevo == constants.estado_archivado:
            p = Postulacion.objects.filter(oportunidad_id = oportunidad.id).update(estado_postulacion = constants.postulacion_finalizado,
                                                                                   fecha_modificacion = datetime.now())
        oportunidad.estado_oportunidad = estado_nuevo
        oportunidad.estado = constants.estado_activo
        oportunidad.usuario_modificacion = user.username
        oportunidad.fecha_modificacion = datetime.now()
        oportunidad.save()

        oportunidad.universidad = universidad
        oportunidad.carrera = carrera
        oportunidad.idioma = idioma
        oportunidad.conocimiento = conocimiento
        oportunidad.beneficio = beneficio
        oportunidad.estado_oportunidad = estado_nuevo
        oportunidad.grado_estudio = grado_estudio
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
    f = request.GET['f']
    objects = Postulacion.objects.filter(oportunidad_id = id, fase_id = int(f))
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
    ids = json.loads(request.GET['ids'])
    ids_estudiante = json.loads(request.GET['ids_estudiante'])
    f = request.GET['f']
    o = request.GET['o']
    id_fase = int(f)

    oportunidad =  get_object_or_404(Oportunidad, pk=o)
    user = request.user
    user = User.objects.get(id = user.id)

    #actualiza a la siguiente fase
    if id_fase > 0:
        estado_postulacion = 'E'
        fase = ProcesoFase.objects.get(pk = id_fase)
        res_postulaciones = Postulacion.objects.filter(pk__in=ids, estado = 'A').update(fase = fase,
                                                                                        estado_postulacion = estado_postulacion,
                                                                                        fecha_modificacion = datetime.now(),
                                                                                        usuario_modificacion = user.username)
        res_oportunidad = Oportunidad.objects.filter(pk = o).update(fase = fase, fecha_modificacion = datetime.now(),
                                                                    usuario_modificacion = user.username)
        enviar_mensaje_multiple_estudiantes(oportunidad, user, ids_estudiante, fase.mensaje_asunto, fase.mensaje_contenido, False, False)

    #inactiva o activa a los seleccionados
    else:
        if id_fase == 0: #fue inactivado
            estado_postulacion = 'F'
            estado_fase = constants.estado_inactivo
            notificacion_asunto = constants.proceso_finalizado_asunto
            # res_postulaciones = Postulacion.objects.filter(pk__in=ids).update(estado_fase = estado_fase,
            #                                                                   fecha_modificacion = datetime.now(),
            #                                                                   usuario_modificacion = user.username)
        if id_fase == -1: #fue reactivado
            estado_postulacion = 'P'
            if oportunidad.fase.id >= 2 and oportunidad.fase.id <= 3:
                estado_postulacion = 'E'
            elif oportunidad.fase.id == 4:
                estado_postulacion = 'F'
            estado_fase = constants.estado_activo
            notificacion_asunto = constants.proceso_reabierto_asunto
        res_postulaciones = Postulacion.objects.filter(pk__in=ids).update(estado_fase = estado_fase,
                                                                          estado_postulacion = estado_postulacion,
                                                                          fecha_modificacion = datetime.now(),
                                                                          usuario_modificacion = user.username)
        enviar_notificacion_multiple_estudiantes(oportunidad, ids_estudiante, notificacion_asunto, False, user.username)
    #define response
    response = {
        'resp': 's'
    }
    #serialize to json
    s = StringIO()
    json.dump(response, s)
    s.seek(0)
    return HttpResponse(s.read())


