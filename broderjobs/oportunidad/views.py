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
from main.models import PeriodosGraduacion
from .models import Oportunidad, Postulacion, ProcesoFase, BeneficioExtra
from estudiante.models import Estudiante
from models import Persona, GradoEstudio, Universidad, Carrera, Pais, Ciudad, TipoPuesto, Idioma, CargaHoraria, TipoRemuneracion, Beneficio, Conocimiento
from empresa.models import Representante, Empresa
from mensaje.models import Mensaje, Mensaje_Destinatario
from mensaje.utils import enviar_mensaje_multiple_estudiantes, enviar_notificacion_multiple_estudiantes
from django.db.models import Q, CharField
from datetime import date, datetime
import json
from cStringIO import StringIO
from .compatibilidad import calcular_compatibilidad, guardar_compatibilidad, actualizar_compatibilidad


# Create your views here.
class OportunidadCrearView(FormView):
    form_class = forms.OportunidadForm
    template_name = 'oportunidad/crear.html'
    success_url = reverse_lazy('empresa-oportunidad-listar')

    def get_context_data(self, **kwargs):
        beneficio =Beneficio.objects.all()
        context = super(OportunidadCrearView, self).get_context_data(**kwargs)
        context['beneficios'] = beneficio
        return context

    def get_initial(self):
        user = self.request.user
        persona = get_object_or_404(Persona, usuario_id=user.id)
        representante = get_object_or_404(Representante, persona_id =persona.id)
        empresa = Empresa.objects.get(id=representante.empresa.id)
        return {'longitud': empresa.longitud, 'latitud': empresa.latitud}

    def form_valid(self, form):
        user_id = self.request.user
        user = get_object_or_404(User, pk = user_id.id)
        persona = get_object_or_404(Persona, usuario_id=user.id)
        representante = get_object_or_404(Representante, persona_id=persona.id)
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
        # beneficio = form.cleaned_data['beneficio']

        beneficios = form.cleaned_data['beneficios_hidden']
        list_beneficios = []
        list_beneficios_extras = []
        list_b = beneficios.split(',')
        for b in list_b:
            try:
                id = int(b)
                beneficio = Beneficio.objects.get(id = id)
                if beneficio is not None:
                    list_beneficios.append(beneficio)
            except Exception:
                list_beneficios_extras.append(b)

        tipo_puesto = form.cleaned_data['tipo_puesto']
        edad_desde = form.cleaned_data['edad_desde']
        edad_hasta = form.cleaned_data['edad_hasta']
        genero = form.cleaned_data['genero']
        grado_estudio = form.cleaned_data['grado_estudio']
        universidad = form.cleaned_data['universidad']
        tipo_carrera = form.cleaned_data['tipo_carrera']
        carrera = form.cleaned_data['carrera']
        idioma = form.cleaned_data['idioma']
        conocimiento = form.cleaned_data['conocimiento']
        longitud = form.cleaned_data['longitud']
        latitud = form.cleaned_data['latitud']

        periodo_graduacion_hidden = form.cleaned_data['periodo_graduacion_hidden']

        if periodo_graduacion_hidden is not None and periodo_graduacion_hidden != '':
            periodo_split = periodo_graduacion_hidden.split(',')
            periodo_desde = periodo_split[0]
            periodo_hasta = periodo_split[1]
        else:
            periodo_desde = ''
            periodo_hasta = ''

        if periodo_desde == '' or periodo_hasta == '':
            periodo_graduacion_desde = None
            periodo_graduacion_hasta = None
        else:
            periodo_graduacion_desde = PeriodosGraduacion.objects.get(id=int(periodo_desde))
            periodo_graduacion_hasta = PeriodosGraduacion.objects.get(id=int(periodo_hasta))

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

        oportunidad.graduacion_desde = periodo_graduacion_desde
        oportunidad.graduacion_hasta = periodo_graduacion_hasta

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

        for be in list_beneficios_extras:
            Be_extra = BeneficioExtra()
            Be_extra.descripcion = be
            Be_extra.oportunidad = oportunidad
            Be_extra.save()

        oportunidad.universidad = universidad
        oportunidad.tipo_carrera = tipo_carrera
        oportunidad.carrera = carrera
        oportunidad.idioma = idioma
        oportunidad.conocimiento = conocimiento
        # oportunidad.beneficio = beneficio
        oportunidad.beneficio = list_beneficios
        oportunidad.grado_estudio = grado_estudio
        oportunidad.save()
        # total = guardar_compatibilidad(oportunidad.carrera.all(), oportunidad.universidad.all(), oportunidad.grado_estudio,
        #                                oportunidad.edad_desde, oportunidad.edad_hasta, oportunidad.pais, oportunidad.ciudad,
        #                                oportunidad.genero, oportunidad.tipo_puesto, oportunidad.carga_horaria,
        #                                oportunidad.idioma, oportunidad.conocimiento, oportunidad.empresa, oportunidad.id)
        resp = guardar_compatibilidad(oportunidad)
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

        beneficios = oportunidad.beneficio.all()

        beneficios_str = ','.join([str(x.id) for x in beneficios]) if beneficios else ''

        beneficios_extra = BeneficioExtra.objects.filter(oportunidad_id=oportunidad.id)

        beneficios_extra_str = ','.join([str(x.id) for x in beneficios_extra]) if beneficios_extra.count() > 0 else ''

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
                # 'beneficio': oportunidad.beneficio,
                'beneficios_hidden': beneficios_str,
                'beneficios_extras_hidden': beneficios_extra_str,
                'beneficios_nuevos_hidden': '',
                'resumen': oportunidad.resumen,
                'carga_horaria': oportunidad.carga_horaria,
                'tipo_puesto': oportunidad.tipo_puesto,
                'estado': oportunidad.estado,
                'estado_oportunidad': oportunidad.estado_oportunidad,
                'edad_desde': oportunidad.edad_desde,
                'edad_hasta': oportunidad.edad_hasta,
                'genero': oportunidad.genero,
                'grado_estudio': oportunidad.grado_estudio,
                'universidad': oportunidad.universidad.all(),
                'tipo_carrera': oportunidad.tipo_carrera,
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

        beneficios = oportunidad.beneficio.all()

        beneficios_extra = BeneficioExtra.objects.filter(oportunidad_id=oportunidad.id)

        beneficios_universo = Beneficio.objects.filter().exclude(id__in = beneficios)

        context['beneficios'] = beneficios
        context['beneficios_extra'] = beneficios_extra
        context['beneficios_universo'] = beneficios_universo

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
        # beneficio = form.cleaned_data['beneficio']
        tipo_puesto = form.cleaned_data['tipo_puesto']

        edad_desde = form.cleaned_data['edad_desde']
        edad_hasta = form.cleaned_data['edad_hasta']
        genero = form.cleaned_data['genero']
        grado_estudio = form.cleaned_data['grado_estudio']
        universidad = form.cleaned_data['universidad']
        tipo_carrera = form.cleaned_data['tipo_carrera']
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

        oportunidad.edad_desde = edad_desde
        oportunidad.edad_hasta = edad_hasta
        oportunidad.genero = genero
        oportunidad.resumen = resumen
        oportunidad.tipo_puesto = tipo_puesto

        oportunidad.estado = constants.estado_activo
        estado_anterior = oportunidad.estado_oportunidad

        beneficios_extras_hidden = form.cleaned_data['beneficios_extras_hidden']
        beneficios_extras_ids = beneficios_extras_hidden.split(',')
        # beneficios_extras = BeneficioExtra.objects.filter(oportunidad_id=oportunidad.id).filter(id__in=beneficios_extras_ids)

        if beneficios_extras_hidden.strip() != '':
            beneficios_extras_ids = beneficios_extras_hidden.split(',')
            beneficios_extras = BeneficioExtra.objects.filter(oportunidad_id=oportunidad.id).filter(id__in=beneficios_extras_ids)

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

        beneficios_hidden = form.cleaned_data['beneficios_hidden']
        beneficios_nuevos_hidden = form.cleaned_data['beneficios_nuevos_hidden']
        beneficios_ids = beneficios_hidden.split(',')
        beneficios_nuevos_ids = beneficios_nuevos_hidden.split(',')
        if '' not in  beneficios_ids and len(beneficios_ids) == 1:
            beneficios = Beneficio.objects.filter(id__in=beneficios_ids)
        else:
            oportunidad.beneficio.all().delete()

        if '_abrir' not in self.request.POST:
            if beneficios_extras_hidden.strip() != '':
                BeneficioExtra.objects.filter(oportunidad_id=oportunidad.id).exclude(id__in = beneficios_extras).delete()
            else:
                BeneficioExtra.objects.filter(oportunidad_id=oportunidad.id).delete()
        else:
            if beneficios_extras_hidden.strip() != '':
                for be in beneficios_extras:
                    be.oportunidad = oportunidad
                    be.save()
            else:
                BeneficioExtra.objects.filter(oportunidad_id=oportunidad.id).delete()

        for be in beneficios_nuevos_ids:
            if be.strip() != '':
                Be_extra = BeneficioExtra()
                Be_extra.descripcion = be
                Be_extra.oportunidad = oportunidad
                Be_extra.save()

        oportunidad.universidad = universidad
        oportunidad.tipo_carrera = tipo_carrera
        oportunidad.carrera = carrera
        oportunidad.idioma = idioma
        oportunidad.conocimiento = conocimiento

        oportunidad.estado_oportunidad = estado_nuevo
        oportunidad.grado_estudio = grado_estudio
        oportunidad.save()
        # total = guardar_compatibilidad(oportunidad.carrera.all(), oportunidad.universidad.all(), oportunidad.grado_estudio,
        #                                oportunidad.edad_desde, oportunidad.edad_hasta, oportunidad.pais, oportunidad.ciudad,
        #                                oportunidad.genero, oportunidad.tipo_puesto, oportunidad.carga_horaria,
        #                                oportunidad.idioma, oportunidad.conocimiento, oportunidad.empresa, oportunidad.id)
        resp = guardar_compatibilidad(oportunidad)
        return super(OportunidadEditarView, self).form_valid(form)

class OportunidadArchivarView(FormView):

    def get(self, request, *args, **kwargs):
        id = request.GET.get('id')
        usuario = User.objects.get(id = self.request.user.id)
        try:
            oportunidad = Oportunidad.objects.get(id = id)
            oportunidad.estado_oportunidad = constants.estado_archivado
            oportunidad.save()
            postulaciones = Postulacion.objects.filter(oportunidad_id=id)
            postulaciones.update(estado_fase =  constants.estado_inactivo,estado_postulacion = constants.postulacion_finalizado,
                                                                          fecha_modificacion = datetime.now(),
                                                                          usuario_modificacion = usuario.username)
            ids_estudiante = postulaciones.values_list('estudiante_id', flat=True).order_by('estudiante_id')
            enviar_notificacion_multiple_estudiantes(oportunidad, ids_estudiante, constants.proceso_finalizado_asunto,
                                                     False, usuario.username)
            response = 'La oportunidad ha sido archivada'
        except :
            response = 'Error al archivar la oportunidad, intente nuevamente.'
        #serialize to json
        s = StringIO()
        json.dump(response, s)
        s.seek(0)
        return HttpResponse(s.read())

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
        enviar_mensaje_multiple_estudiantes(oportunidad, user, ids_estudiante, fase.mensaje_asunto,
                                            fase.mensaje_contenido, False, None)

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

def total_compatibles(request):
    carrera         = request.POST.get('carrera').split(",")
    universidad     = request.POST.get('universidad').split(",")
    grado_estudio   = request.POST.get('grado_estudio')
    edad_desde      = request.POST.get('edad_desde')
    edad_hasta      = request.POST.get('edad_hasta')
    pais            = request.POST.get('pais')
    ciudad          = request.POST.get('ciudad')
    genero          = request.POST.get('genero')
    tipo_puesto     = request.POST.get('tipo_puesto')
    carga_horaria   = request.POST.get('carga_horaria')
    idioma          = request.POST.get('idioma')
    conocimiento    = request.POST.get('conocimiento')
    remuneracion_min    = request.POST.get('remuneracion_min')
    remuneracion_max    = request.POST.get('remuneracion_max')
    remuneracion_min    = request.POST.get('remuneracion_min')
    remuneracion_max    = request.POST.get('remuneracion_max')

    user = get_object_or_404(User, pk = request.user.id)
    persona = get_object_or_404(Persona, usuario_id=user.id)
    representante =get_object_or_404(Representante, persona_id=persona.id)

    # id              = request.GET.get('id')
    # carrera         = request.GET.get('carrera')
    # universidad     = request.GET.get('universidad')
    # grado_estudio   = request.GET.get('grado_estudio')
    # # perido = request.GET.get('carrera')
    # edad_desde      = request.GET.get('edad_desde')
    # edad_hasta      = request.GET.get('edad_hasta')
    # pais            = request.GET.get('pais')
    # ciudad          = request.GET.get('ciudad')
    # genero          = request.GET.get('genero')
    # tipo_puesto     = request.GET.get('tipo_puesto')
    # carga_horaria   = request.GET.get('carga_horaria')
    # remuneracion    = request.GET.get('remuneracion')
    # idioma          = request.GET.get('idioma')
    # conocimiento    = request.GET.get('conocimiento')
    # # experiencia     = request.GET.get('conocimiento')
    total = calcular_compatibilidad(carrera, universidad, grado_estudio, edad_desde, edad_hasta, pais, ciudad, genero,
                                    tipo_puesto, carga_horaria, idioma, conocimiento, remuneracion_min, remuneracion_max,
                                    representante.empresa.id)
    data = json.dumps(total)
    return HttpResponse(data, content_type='application/json')

def actualizar_compatibilidad_estudiante(request):
    persona = get_object_or_404(Persona, usuario_id = request.user.id)
    estudiante = get_object_or_404(Estudiante, persona_id= persona)

    resp = actualizar_compatibilidad(estudiante)
    data = json.dumps(resp)
    return HttpResponse(data, content_type='application/json')


