
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from .forms import RegistroCV
from django.views.generic import TemplateView,FormView
from django.core.urlresolvers import reverse_lazy
from .models import Estudiante
from models import Persona, GradoEstudio, Universidad, Carrera, Pais, Ciudad


@login_required(login_url='/estudiante-registro/')
def registro_cv(request):

    if request.method == 'POST':
        form = RegistroCV(request.POST)
        if form.is_valid():
            user = request.user
            persona = Persona.objects.get(usuario_id=user.id)
            grado_estudio = form.cleaned_data['grado_estudio']
            universidad = form.cleaned_data['universidad']
            carrera = form.cleaned_data['carrera']
            pais =  form.cleaned_data['pais']
            ciudad = form.cleaned_data['ciudad']
            estudiante = Estudiante()
            estudiante.persona = persona
            estudiante.grado_estudio = grado_estudio
            estudiante.universidad = universidad
            estudiante.carrera = carrera
            estudiante.pais = pais
            estudiante.ciudad = ciudad
            estudiante.save()
            return redirect('oportunidad_listar')
    else:
        form = RegistroCV()
    return render(request, 'estudiante/registro-cv.html', {'form': form})

@login_required(login_url='/estudiante-registro/')
def oportunidad_listar(request):
    return render(request, 'estudiante/oportunidad-listar.html')