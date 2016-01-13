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
from .utils import enviar_mensaje
from oportunidad.models import Oportunidad, Postulacion
from .models import Notificacion

# Create your views here.
def buzon_entrada(request):
    # return render_to_response('main/home-estudiante.html',context_instance=RequestContext(request))
    return render_to_response('mensaje/mensaje.html',
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
    # data = serializers.serialize('json', mensaje,
    #                                  fields=('asunto','contenido','fecha_creacion'))
    response = {
        'asunto': mensaje.asunto,
        'contenido': mensaje.contenido,
        'fecha_creacion': str(mensaje.fecha_creacion)
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
    o = request.POST['o']
    p = request.POST['p']
    permite_respuesta = False
    if p == 'S':
        permite_respuesta = True


    oportunidad =  get_object_or_404(Oportunidad, pk=o)
    user = request.user
    user = User.objects.get(id = user.id)
    asunto = "La Empresa " + oportunidad.empresa.nombre + " te ha enviado un mensaje."
    enviar_mensaje(oportunidad, user, ids_estudiante, asunto, contenido, permite_respuesta, False)
    #define response
    response = {
        'resp': '¡Mensaje enviado con exito!'
    }
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