from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, HttpResponseRedirect, render
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from  django.utils.dateparse import parse_date

from django.views.generic import TemplateView,FormView
from django.core.urlresolvers import reverse_lazy
from .models import Persona
from django.core.context_processors import csrf


class EstudianteResgistro(FormView):
    template_name = 'main/estudiante-registro.html'
    form_class = RegisterForm
    success_url = reverse_lazy('registro-cv')

    def form_valid(self, form):
        user = form.save()
        persona = Persona()
        persona.usuario = user
        persona.fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
        dia  = form.cleaned_data['dia']
        mes  = form.cleaned_data['mes']
        ano  = form.cleaned_data['ano']
        nacimiento = parse_date(ano + '-' + mes + '-' + dia)
        persona.fecha_nacimiento = nacimiento
        persona.tipo_persona = "E"
        persona.save()
        return super(EstudianteResgistro, self).form_valid(form)

class EmpresaRegistro(FormView):
    template_name = 'main/empresa-registro.html'
    form_class = RegisterForm
    success_url = reverse_lazy('empresa_registro')

    def form_valid(self, form):
        user = form.save()
        persona = Persona()
        persona.usuario = user
        persona.tipo_persona = "R"
        persona.save()
        return super(EmpresaRegistro, self).form_valid(form)

def login_page(request):
    message = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(username=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    message = "Te haz identificado de modo correcto"
                    return redirect('oportunidad_listar')
                else:
                    message = "tu usuario esta inactivo"
            else:
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
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    message = "Te haz identificado de modo correcto"
                    return redirect('empresa')
                else:
                    message = "tu usuario esta inactivo"
            else:
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
    return render_to_response('main/index-empresa.html',
                              context_instance=RequestContext(request))
def logout_view(request):
    logout(request)
    return redirect('homepage')

def register_user(request):
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
            return redirect('registro_cv')
    else:
        form = RegisterForm()
    return render(request, 'main/estudiante-registro.html', {'form': form})


