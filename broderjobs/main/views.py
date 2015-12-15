# coding=utf-8
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, HttpResponseRedirect, render
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from  django.utils.dateparse import parse_date
from django.contrib.auth.models import User
from django.views.generic import TemplateView,FormView
from django.core.urlresolvers import reverse_lazy, reverse
from .models import Persona
from . import forms
from empresa.models import Representante, Empresa
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
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
                try:
                    persona = Persona.objects.get(usuario_id=user.id, tipo_persona= "E")
                except persona.DoesNotExist:
                    persona = None
                if persona is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect('estudiante-oportunidad-listar')
                    else:
                        message = "Tu usuario esta inactivo"

            message = "Email o contraseña incorrecta"
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
                persona = Persona()
                try:
                    persona = Persona.objects.get(usuario_id=user.id, tipo_persona="R")
                except persona.DoesNotExist:
                    persona = None
                if persona is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect('empresa-oportunidad-listar')
                    else:
                        message = "tu usuario esta inactivo"
            message = "Email o contraseña incorrecta"
    else:
        form = LoginForm()

    return render_to_response('main/empresa-login.html',{'message': message,'form': form},
                                  context_instance=RequestContext(request))

def homepage1(request):
    # return render_to_response('main/home-estudiante.html',context_instance=RequestContext(request))
    return render_to_response('main/estudiante.html',
                              context_instance=RequestContext(request))
def homepage(request):
    message = None
    if request.method == "POST":
        login_form = LoginForm(request.POST, prefix='login')
        registro_form = RegisterForm(request.POST, prefix='registro')
        if '_login' in request.POST:
            if login_form.is_valid():
                user = authenticate(username=request.POST["login-email"], password= request.POST["login-password"])
                if user is not None:
                    persona = Persona()
                    try:
                        persona = Persona.objects.get(usuario_id=user.id, tipo_persona= "E")
                    except persona.DoesNotExist:
                        persona = None
                    if persona is not None:
                        if user.is_active:
                            login(request, user)
                            return redirect('estudiante-oportunidad-listar')
                        else:
                            message = "Tu usuario esta inactivo"

                message = "Email o contraseña incorrecta"

        if '_registro' in request.POST:
            if registro_form.is_valid():
                user = registro_form.save()
                persona = Persona()
                persona.usuario = user
                persona.fecha_nacimiento = registro_form.cleaned_data['fecha_nacimiento']
                dia = registro_form.cleaned_data['dia']
                mes  = registro_form.cleaned_data['mes']
                ano  = registro_form.cleaned_data['ano']
                fecha = parse_date(ano + '-' + mes + '-' + dia)
                persona.fecha_nacimiento = fecha
                persona.tipo_persona = "E"
                persona.save()
                new_user = authenticate(username=request.POST['registro-email'],
                                        password=request.POST['registro-password1'])
                login(request, new_user)
                return redirect('registro-cv')
    else:
        login_form = LoginForm(prefix='login')
        registro_form = RegisterForm(prefix='registro')

    return render_to_response('main/home-estudiante.html', {'message': message, 'login_form': login_form , 'registro_form': registro_form },
                                  context_instance=RequestContext(request))

def homepage_empresa(request):
    message = None
    if request.method == "POST":
        login_form = LoginForm(request.POST, prefix='login')
        registro_form = RegisterForm(prefix='registro')
        if '_login' in request.POST:
            if login_form.is_valid():
                email = request.POST["login-email"]
                password = request.POST["login-password"]
                user = authenticate(username=email, password=password)
                if user is not None:
                    persona = Persona()
                    try:
                        persona = Persona.objects.get(usuario_id=user.id, tipo_persona="R")
                    except persona.DoesNotExist:
                        persona = None
                    if persona is not None:
                        if user.is_active:
                            login(request, user)
                            return redirect('empresa-oportunidad-listar')
                        else:
                            message = "tu usuario esta inactivo"
                message = "Email o contraseña incorrecta"
        if '_registro' in request.POST:
            if registro_form.is_valid():
                print("registro")
                user = registro_form.save()
                persona = Persona()
                persona.usuario = user
                persona.tipo_persona = "R"
                persona.telefono = registro_form.cleaned_data['telefono']
                empresa = registro_form.cleaned_data['empresa']
                persona.save()
                representante = Representante()
                representante.persona = persona
                representante.empresa = empresa
                representante.save()
                new_user = authenticate(username=request.POST['registro-email'], password=request.POST['registro-password1'])
                login(request, new_user)
                mensaje = "Se ha registrado satisfactoriamente"
                return redirect('empresa-oportunidad-listar')
    else:
        login_form = LoginForm(prefix='login')
        registro_form = RegisterForm(prefix='registro')
    return render_to_response('main/home-empresa.html', {'message': message, 'login_form': login_form , 'registro_form': registro_form },
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
            empresa = form.cleaned_data['empresa']
            persona.save()
            representante = Representante()
            representante.persona = persona
            representante.empresa = empresa
            representante.save()
            new_user = authenticate(username=request.POST['email'], password=request.POST['password1'])
            login(request, new_user)
            mensaje = "Se ha registrado satisfactoriamente"
            return redirect('empresa-oportunidad-listar')
    else:
        form = RegisterForm()
    return render(request, 'main/empresa-registro.html', {'form': form, 'mensaje': mensaje})

class ConfiguracionView(TemplateView):
    template_name = 'main/configuracion.html'
    def get_context_data(self, **kwargs):
        user = self.request.user
        usuario = User.objects.get(pk=user.id)
        persona = Persona.objects.get(usuario_id=usuario.id)

        context = super(ConfiguracionView, self).get_context_data(**kwargs)
        context['usuario'] = user
        context['persona'] = persona
        return context


# def editar_usuario(request):
#
#     if request.method == 'POST':
#         form = forms.EditarUsuarioForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#     else:
#         form = forms.EditarUsuarioForm(instance=request.user)
#     return render_to_response('main/editar-cuenta.html',{'form': form},
#                               context_instance=RequestContext(request))

def editar_cuenta(request, template_name='main/editar-cuenta.html',
                    post_change_redirect=None):
    if post_change_redirect is None:
        post_change_redirect = reverse_lazy('homepage')
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(post_change_redirect)
    else:
        form = forms.EditarUsuarioForm(request.user)

    return render_to_response(template_name, {
        'form': form,
    }, context_instance=RequestContext(request))





