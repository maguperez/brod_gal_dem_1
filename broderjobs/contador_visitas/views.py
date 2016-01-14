from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, HttpResponseRedirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse
from datetime import date, datetime
import json
from cStringIO import StringIO
from oportunidad.models import Oportunidad, Postulacion
from .models import VisitasOportunidad
from datetime import date, datetime

def oportunidad_enviar( request ):
    id = request.GET['id']
    if request.user.is_authenticated():
        usuario = request.user.username
    else:
        usuario = None
    oportunidad = get_object_or_404(Oportunidad, pk = id)
    contador = VisitasOportunidad()
    contador.oportunidad = oportunidad
    contador.usuario_creacion = usuario
    contador.ip = get_ip(request)
    contador.fecha_creacion = datetime.now()
    contador.save()

    total = VisitasOportunidad.objects.filter(oportunidad_id = id).count()
    response = {
        'total': total
    }
    #serialize to json
    s = StringIO()
    json.dump(response, s)
    s.seek(0)
    return HttpResponse(s.read())
    # return HttpResponse(data, content_type='application/json')

def get_ip(request):
    """Returns the IP of the request, accounting for the possibility of being
    behind a proxy.
    """
    ip = request.META.get("HTTP_X_FORWARDED_FOR", None)
    if ip:
        # X_FORWARDED_FOR returns client1, proxy1, proxy2,...
        ip = ip.split(", ")[0]
    else:
        ip = request.META.get("REMOTE_ADDR", "")
    return ip

def oportunidad_obtener(request):
    id = request.GET['id']
    total = VisitasOportunidad.objects.filter(oportunidad_id = id).count()
    data = []
    response = {
        'total': total
    }
    data.append(('total', total))
    data_json = json.dumps(response)
    # #serialize to json
    # s = StringIO()
    # json.dump(response, s)
    # s.seek(0)
    # return HttpResponse(s.read())
    return HttpResponse(data_json, content_type='application/json')
