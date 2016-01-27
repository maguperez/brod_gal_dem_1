from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, HttpResponseRedirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse
from datetime import date, datetime
import json
from cStringIO import StringIO
from oportunidad.models import Oportunidad, Postulacion
from .models import Pregunta, Respuesta
from datetime import date, datetime


def preguntas_estudiante(request):
    preguntas = []
    respuestas = []
    Preg = Pregunta.objects.filter()
    for p in Preg:
        respuestas = []
        for r in Respuesta.objects.filter(pregunta_id = p.id):
            respuesta={'id': r.id, 'descripcion': r.descripcion, 'letra':r.letra}
            respuestas.append(respuesta)
        pregunta = {'id': p.id, 'descripcion': p.descripcion, 'respuestas': respuestas }
        preguntas.append(pregunta)

    data = json.dumps(preguntas)
    return HttpResponse(data, content_type='application/json')

def formulario_estudiante(request):
    preguntas = []
    respuestas = []
    Preg = Pregunta.objects.filter()[:3]
    for p in Preg:
        respuestas = []
        for r in Respuesta.objects.filter(pregunta_id = p.id):
            respuesta={'id': r.id, 'descripcion': r.descripcion, 'letra':r.letra}
            respuestas.append(respuesta)
        pregunta = {'id': p.id, 'descripcion': p.descripcion, 'respuestas': respuestas }
        preguntas.append(pregunta)
    return render_to_response('disc/formulario-estudiante.html',{'preguntas': preguntas},
                              context_instance=RequestContext(request))