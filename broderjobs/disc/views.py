from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, HttpResponseRedirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse
from datetime import date, datetime
import json
from cStringIO import StringIO
from oportunidad.models import Oportunidad, Postulacion
from .models import Pregunta, Respuesta, EstudianteRespuestas
from estudiante.models import Estudiante
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

def respuesta_estudiante(request):
    pregunta_id = request.POST['p']
    resp_mas_id = request.POST['r_mas']
    resp_menos_id = request.POST['r_menos']
    estudiante = Estudiante.objects.get(persona__usuario = request.user.id)
    try:
        pregunta = Pregunta.objects.get(id = pregunta_id)
        c = EstudianteRespuestas.objects.get(id_pregunta = pregunta.id, estudiante_id = estudiante.id).delete()
        respuesta_mas = Respuesta.objects.get(id = resp_mas_id, pregunta_id = pregunta_id)
        respuesta_menos = Respuesta.objects.get(id = resp_menos_id, pregunta_id = pregunta_id)
        resp_estudiante = EstudianteRespuestas()
        resp_estudiante.estudiante = estudiante
        resp_estudiante.pregunta = pregunta
        resp_estudiante.letra_mas = respuesta_mas.letra
        resp_estudiante.letra_menos = respuesta_menos.letra
        resp_estudiante.save()
        estudiante.completo_test = True
        estudiante.save()
        data = "0"
    except Exception, e:
        resp = EstudianteRespuestas.objects.filter(estudiante_id = estudiante.id).delete()
        data = str(e)

    data = json.dumps(data)
    return HttpResponse(data, content_type='application/json')
