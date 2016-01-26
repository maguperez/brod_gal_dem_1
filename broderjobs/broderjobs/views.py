
# coding=utf-8
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, HttpResponseRedirect, render
from django.contrib.auth import authenticate, login, logout
from  django.utils.dateparse import parse_date
from django.contrib.auth.models import User
from django.views.generic import TemplateView,FormView
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from main.models import Persona
from estudiante.models import Estudiante



def error404(request):
    return render(request,'404.html')


def login_facebook(request):
    user = request.user
    persona = Persona.objects.get(usuario_id = user.id)
    if persona.tipo_persona == 'E':
        if Estudiante.objects.filter(persona=persona).exists():
            return redirect('estudiante-oportunidad-listar')
        else:
            return redirect('estudiante-registro-cv')

    return render_to_response('404.html',
                              context_instance=RequestContext(request))