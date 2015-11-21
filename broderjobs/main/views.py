# coding=utf-8
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, HttpResponseRedirect, render
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from  django.utils.dateparse import parse_date

from django.views.generic import TemplateView,FormView
from django.core.urlresolvers import reverse_lazy
from .models import Persona
from empresa.models import Representante, Empresa
from django.core.context_processors import csrf


def login_estudiante(request):
    message = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(username=email, password=password)
            if user is not None:
                persona = Persona.objects.get(usuario_id=user.id, tipo_persona= "E")
                if persona is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect('oportunidad-listar')
                    else:
                        message = "tu usuario esta inactivo"

            message = "Email o contraea incorrecta"
    else:
        form = LoginForm()

    return render_to_response('main/estudiante-login.html',{'message': message,'form': form},
                                  context_instance=RequestContext(request))

def empresa_login(request):
    message = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(username=email, password=password)
            if user is not None:
                persona = Persona.objects.get(usuario_id=user.id, tipo_persona= "E")
                if persona is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect('oportunidad-listar')
                    else:
                        message = "tu usuario esta inactivo"
            message = "Email o contraea incorrecta"
    else:
        form = LoginForm()

    return render_to_response('main/empresa-login.html',{'message': message,'form': form},
                                  context_instance=RequestContext(request))

def homepage(request):
    return render_to_response('main/estudiante.html',
                              context_instance=RequestContext(request))
def estudiante(request):
    return render_to_response('main/estudiante.html',
                              context_instance=RequestContext(request))
def empresa(request):
    return render_to_response('main/empresa.html',
                              context_instance=RequestContext(request))
def estudiante_registro(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            persona = Persona()
            persona.usuario = user
            persona.fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            dia = form.cleaned_data['dia']
            mes  = form.cleaned_data['mes']
            ano  = form.cleaned_data['ano']
            fecha = parse_date(ano + '-' + mes + '-' + dia)
            persona.fecha_nacimiento = fecha
            persona.tipo_persona = "E"
            persona.save()
            new_user = authenticate(username=request.POST['email'],
                                    password=request.POST['password1'])
            login(request, new_user)
            return redirect('registro-cv')
    else:
        form = RegisterForm()
    return render(request, 'main/estudiante-registro.html', {'form': form})

def empresa_registro(request):
    mensaje = None
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            persona = Persona()
            persona.usuario = user
            persona.tipo_persona = "R"
            persona.telefono = form.cleaned_data['telefono']
            e = form.cleaned_data['empresa']
            print(e)
            empresa = Empresa.objects.get(id=e)
            print(empresa)
            persona.save()
            representante = Representante()
            representante.persona = persona
            representante.empresa = empresa
            representante.save()
            new_user = authenticate(username=request.POST['email'], password=request.POST['password1'])
            login(request, new_user)
            mensaje = "Se ha registrado satisfactoriamente"
            return redirect('empresa_oportunidad_listar')
    else:
        form = RegisterForm()
    return render(request, 'main/empresa-registro.html', {'form': form, 'mensaje': mensaje})


