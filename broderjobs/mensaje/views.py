# coding=utf-8
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, HttpResponseRedirect, render, get_object_or_404
from .models import  Mensaje_Destinatario, Mensaje
from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse
from datetime import date, datetime
import json
from cStringIO import StringIO
from django.views.generic import TemplateView, FormView
from .utils import enviar_mensaje, enviar_mensaje_multiple_estudiantes, obtener_imagen_persona
from oportunidad.models import Oportunidad, Postulacion
from .models import Notificacion
from main.models import Persona
from empresa.models import Empresa, Representante
from estudiante.models import Estudiante
from main.utils import LoginRequiredMixin

# Create your views here.
def buzon_entrada(request):
    # return render_to_response('main/home-estudiante.html',context_instance=RequestContext(request))
    user = request.user
    persona = Persona.objects.get(usuario_id=user.id)
    representante = Representante.objects.get(persona_id =persona.id)
    empresa = Empresa.objects.get(id=representante.empresa.id)
    oportunidades =  Oportunidad.objects.filter(empresa_id = empresa.id).order_by("fecha_publicacion")
    return render_to_response('mensaje/mensaje.html', {'oportunidades' : oportunidades},
                              context_instance=RequestContext(request))
# Create your views here.
def mensaje_crear(request):
    # return render_to_response('main/home-estudiante.html',context_instance=RequestContext(request))
    return render_to_response('mensaje/mensaje-crear.html',
                              context_instance=RequestContext(request))

def mensaje_ver( request ):
    id = request.GET['id']
    destinatario= Mensaje_Destinatario.objects.get(id = id)
    mensaje = Mensaje.objects.get(id = destinatario.mensaje.id)
    resp_dest = Mensaje_Destinatario.objects.filter(id = destinatario.id).update(fecha_leido = datetime.now(), leido = True)
    resp_not = Notificacion.objects.filter(usuario_destinatario = destinatario.usuario_destinatario.id).update(
                                                                                fecha_leido = datetime.now(), leido = True)
    response = {
        'asunto': mensaje.asunto,
        'contenido': mensaje.contenido,
        'fecha_creacion': str(mensaje.fecha_creacion),
        'empresa': mensaje.oportunidad.empresa.nombre,
        'empresa_id': str(mensaje.oportunidad.empresa.id),
        'mensaje_destinatario_id': str(destinatario.id),
        'usuario_id': str(mensaje.usuario_remitente.id),
        'permite_respuesta': str(mensaje.permite_respuesta),
    }
    #serialize to json
    s = StringIO()
    json.dump(response, s)
    s.seek(0)
    return HttpResponse(s.read())
    # return HttpResponse(data, content_type='application/json')

def mensaje_enviar_estudiantes( request ):
    ids = json.loads(request.POST['ids'])
    ids_estudiante = json.loads(request.POST['ids_estudiante'])
    contenido = request.POST['c']
    id_oportunidad = request.POST['o']
    p = request.POST['p']
    permite_respuesta = False
    if p == 'S':
        permite_respuesta = True
    oportunidad =  get_object_or_404(Oportunidad, pk=id_oportunidad)
    userio_remitente = User.objects.get(id = request.user.id)
    asunto = "La Empresa " + oportunidad.empresa.nombre + " te ha enviado un mensaje."
    enviar_mensaje_multiple_estudiantes(oportunidad, userio_remitente, ids_estudiante, asunto, contenido, permite_respuesta, None)
    #define response
    response = {'resp': '¡Mensaje enviado con exito!'}
    #serialize to json
    s = StringIO()
    json.dump(response, s)
    s.seek(0)
    return HttpResponse(s.read())

def mensaje_enviar( request ):
    id_empresa = json.loads(request.POST['id'])
    contenido = request.POST['c']
    id_oportunidad = request.POST['id_o']
    id_postulacion = request.POST['id_p']
    id_mensaje_destinatario = request.POST['id_md']
    id_usuario_destinatario = request.POST['id_u']
    pr = request.POST['pr']
    permite_respuesta = False
    if pr == 'S':
        permite_respuesta = True
    try:
        postulacion = Postulacion.objects.get(pk=id_postulacion)
    except Postulacion.DoesNorExist:
        postulacion = None
    try:
        mensaje_previo=  Mensaje_Destinatario.objects.get(pk=id_mensaje_destinatario)
    except Mensaje.DoesNotExist:
        mensaje_previo = None
    oportunidad =  get_object_or_404(Oportunidad, pk=id_oportunidad)

    # usuario logueado es el ue envia
    usuario_remitente = User.objects.get(id = request.user.id)

    # Id Usuario a enviar mensaje
    usuario_destinatario = User.objects.get(id = id_usuario_destinatario)

    asunto =  postulacion.estudiante.persona.usuario.first_name +" "+postulacion.estudiante.persona.usuario.last_name +\
              " le ha enviado un mensaje."

    enviar_mensaje(oportunidad, usuario_remitente, usuario_destinatario, asunto, contenido, permite_respuesta, mensaje_previo)
    #define response
    response = {'resp': '¡Mensaje enviado con exito!'}
    #serialize to json
    s = StringIO()
    json.dump(response, s)
    s.seek(0)
    return HttpResponse(s.read())

def mensaje_notificacion_vista( request ):
    id = json.loads(request.GET['id'])
    n = Notificacion.objects.filter(usuario_destinatario_id = id).update(leido = True, fecha_leido = datetime.now(),
                                                                         fecha_modificacion = datetime.now())
    #define response
    response = {
        'resp': 'visto con exito'
    }
    #serialize to json
    s = StringIO()
    json.dump(response, s)
    s.seek(0)
    return HttpResponse(s.read())

class MensajeBuscarView(LoginRequiredMixin, TemplateView):

    def get(self, request, *args, **kwargs):
        id = request.GET.get('id')
        user = request.user
        persona = Persona.objects.get(usuario_id=user.id)
        representante = get_object_or_404(Representante, persona_id =persona.id)
        if id != '0':
            list_mensajes = Mensaje_Destinatario.objects.filter(mensaje__oportunidad= id,
                                                                usuario_destinatario_id = user.id,
                                                                estado = 'A').order_by("-fecha_creacion")
        else:
           list_mensajes = Mensaje_Destinatario.objects.filter(usuario_destinatario_id = user.id,
                                                               estado = 'A').order_by("-fecha_creacion")
        mensajes = []
        for m in list_mensajes:
            try:
                persona = Persona.objects.get(usuario_id =  m.mensaje.usuario_remitente.id)
                foto = obtener_imagen_persona(persona)
                mensaje = {'id': m.id,
                           'usuario_remitente': persona,
                           'foto': foto,
                           'fecha_envio': m.fecha_envio,
                           'asunto': m.mensaje.asunto,
                           'contenido': m.mensaje.contenido}
                mensajes.append(mensaje)
            except Persona.DoesNotExist:
                pass

        return render_to_response('mensaje/mensaje-listar.html', {'mensajes': mensajes},
                                  context_instance = RequestContext(request))

class MensajeAbrirConRelacionados(LoginRequiredMixin, TemplateView):

    def get(self, request, *args, **kwargs):
        id = request.GET.get('id')
        # user = request.user
        # persona = Persona.objects.get(usuario_id=user.id)
        # representante = get_object_or_404(Representante, persona_id =persona.id)
        if id != '0':
            m_actual = get_object_or_404(Mensaje_Destinatario, pk= id)
            persona_mensaje_actual = Persona.objects.get(usuario_id =  m_actual.mensaje.usuario_remitente.id)
            foto_persona_actual = obtener_imagen_persona(persona_mensaje_actual)
            mensaje_actual = {'id': m_actual.id,
                              'remitente': persona_mensaje_actual,
                              'foto': foto_persona_actual,
                              'fecha_envio': m_actual.fecha_envio,
                              'asunto': m_actual.mensaje.asunto,
                              'contenido': m_actual.mensaje.contenido}
            list_mensajes = m_actual.get_anteriores().order_by('-fecha_creacion')

        mensajes_anteriores = []
        for m in list_mensajes:
            persona = Persona.objects.get(usuario_id =  m.mensaje.usuario_remitente.id)
            foto = obtener_imagen_persona(persona)
            mensaje = {'id': m.id,
                       'remitente': persona,
                       'foto': foto,
                       'fecha_envio': m.fecha_envio,
                       'asunto': m.mensaje.asunto,
                       'contenido': m.mensaje.contenido}
            mensajes_anteriores.append(mensaje)
        return render_to_response('mensaje/mensaje-relacionados-listar.html', {'mensaje_actual':mensaje_actual,
                                                                               'mensajes_anteriores': mensajes_anteriores},
                                  context_instance = RequestContext(request))