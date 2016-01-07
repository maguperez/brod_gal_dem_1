from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, HttpResponseRedirect, render
from .models import  Mensaje_Destinatario, Mensaje
from django.core import serializers
from django.http import HttpResponse
from datetime import date, datetime
import json
from cStringIO import StringIO

# Create your views here.
def buzon_entrada(request):
    # return render_to_response('main/home-estudiante.html',context_instance=RequestContext(request))
    return render_to_response('mensaje.html',
                              context_instance=RequestContext(request))
# Create your views here.
def mensaje_crear(request):
    # return render_to_response('main/home-estudiante.html',context_instance=RequestContext(request))
    return render_to_response('mensaje-crear.html',
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