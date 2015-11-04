
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout

from django.views.generic import TemplateView,FormView
from django.core.urlresolvers import reverse_lazy

@login_required(login_url='/estudiante_registro/')
def RegistroCV(request):
    return render_to_response('estudiante/registro.html',
                              context_instance=RequestContext(request))
