# coding=utf-8
import json
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, HttpResponseRedirect, render
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from  django.utils.dateparse import parse_date
from django.contrib.auth.models import User
from django.views.generic import TemplateView,FormView
from django.core.urlresolvers import reverse_lazy, reverse
from .models import Persona, Ciudad, Pais, Carrera, TipoCarrera, PeriodosGraduacion, Universidad
from . import forms
from empresa.models import Representante, Empresa
from main.utils import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.core.context_processors import csrf
from django.core import serializers
from django.db.models import Q

def homepage1(request):
    # return render_to_response('main/home-estudiante.html',context_instance=RequestContext(request))
    return render_to_response('main/estudiante.html',
                              context_instance=RequestContext(request))

def home(request):
    message_registro = None
    message_login = None
    if request.user.is_authenticated():
        persona = Persona()
        try:
            persona = Persona.objects.get(usuario_id=request.user.id)
        except persona.DoesNotExist:
            persona = None
        if persona is not None:
            if persona.tipo_persona == 'E':
                return redirect('estudiante-oportunidad-listar')
            if persona.tipo_persona == 'R':
                return redirect('empresa-oportunidad-listar')
        else:
            login_form = LoginForm(prefix='login')
            registro_form = RegisterForm(prefix='registro')
        return render_to_response('main/home-estudiante.html', {'message_login': message_login,
                                                                'message_registro': message_registro,
                                                                'login_form': login_form ,
                                                                'registro_form': registro_form },
                                      context_instance=RequestContext(request))
    else:
        if request.method == "POST":
            login_form = LoginForm(request.POST, prefix='login')
            registro_form = RegisterForm(request.POST, prefix='registro')
            if '_login' in request.POST:
                if login_form.is_valid():
                    if not login_form.cleaned_data['remember_me']:
                        request.session.set_expiry(0)
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
                                message_login = "Tu usuario esta inactivo"

                    message_login = "Email o contraseña incorrecta"

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
                    message_registro= "Error al registrar"
        else:
            login_form = LoginForm(prefix='login')
            registro_form = RegisterForm(prefix='registro')

        return render_to_response('main/home.html', {'message_login': message_login,
                                                                'message_registro': message_registro,
                                                                'login_form': login_form ,
                                                                'registro_form': registro_form },
                                      context_instance=RequestContext(request))

def home_empresa(request):
    message = None
    if request.user.is_authenticated():
        return redirect('empresa-oportunidad-listar')
    else:
        if request.method == "POST":
            login_form = LoginForm(request.POST, prefix='login')
            registro_form = RegisterForm(request.POST, prefix='registro')
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
        return render_to_response('main/inicio-empresa.html', {'message': message, 'login_form': login_form , 'registro_form': registro_form },
                                      context_instance=RequestContext(request))

def homepage(request):
    message_registro = None
    message_login = None
    if request.user.is_authenticated():
        persona = Persona()
        try:
            persona = Persona.objects.get(usuario_id=request.user.id)
        except persona.DoesNotExist:
            persona = None
        if persona is not None:
            if persona.tipo_persona == 'E':
                return redirect('estudiante-oportunidad-listar')
            if persona.tipo_persona == 'R':
                return redirect('empresa-oportunidad-listar')
        else:
            login_form = LoginForm(prefix='login')
            registro_form = RegisterForm(prefix='registro')
        return render_to_response('main/home-estudiante.html', {'message_login': message_login,
                                                                'message_registro': message_registro,
                                                                'login_form': login_form ,
                                                                'registro_form': registro_form },
                                      context_instance=RequestContext(request))
    else:
        if request.method == "POST":
            login_form = LoginForm(request.POST, prefix='login')
            registro_form = RegisterForm(request.POST, prefix='registro')
            if '_login' in request.POST:
                if login_form.is_valid():
                    if not login_form.cleaned_data['remember_me']:
                        request.session.set_expiry(0)
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
                                message_login = "Tu usuario esta inactivo"

                    message_login = "Email o contraseña incorrecta"

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
                    message_registro= "Error al registrar"
        else:
            login_form = LoginForm(prefix='login')
            registro_form = RegisterForm(prefix='registro')

        return render_to_response('main/home-estudiante.html', {'message_login': message_login,
                                                                'message_registro': message_registro,
                                                                'login_form': login_form ,
                                                                'registro_form': registro_form },
                                      context_instance=RequestContext(request))

def homepage_empresa(request):
    message = None
    if request.user.is_authenticated():
        return redirect('empresa-oportunidad-listar')
    else:
        if request.method == "POST":
            login_form = LoginForm(request.POST, prefix='login')
            registro_form = RegisterForm(request.POST, prefix='registro')
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

class UsuariosView(TemplateView):
    template_name = 'main/usuarios.html'
    def get_context_data(self, **kwargs):
        user = self.request.user
        persona = Persona.objects.get(usuario_id=user)
        representante = Representante.objects.get(persona_id=persona.id)
        usuarios = None
        if persona.tipo_persona == 'R':
            tipo = True
            representantes = Representante.objects.filter(empresa_id = representante.empresa.id, estado = 'A')
        else:
            tipo = False
        context = super(UsuariosView, self).get_context_data(**kwargs)
        context['usuario'] = user
        context['usuarios'] = usuarios
        context['representantes'] = representantes
        context['tipo'] = tipo
        return context

class CuentaEditarView(LoginRequiredMixin, FormView):
    template_name = 'main/cuenta-editar.html'
    form_class = forms.CuentaEditarForm
    success_url = reverse_lazy('cuenta-editar')

    def get_initial(self):
        user = self.request.user
        persona = Persona.objects.get(usuario_id=user.id)
        return {'first_name': persona.usuario.first_name,
                'last_name': persona.usuario.last_name,
                'email': persona.usuario.email,
                'telefono': persona.telefono,}
    def get_context_data(self, **kwargs):
        user = self.request.user
        persona = Persona.objects.get(usuario_id=user.id)
        if persona.tipo_persona == 'R':
            tipo = True
        else:
            tipo = False
        context = super(CuentaEditarView, self).get_context_data(**kwargs)
        context['tipo'] = tipo
        return context


    def form_valid(self, form):
        user = self.request.user
        usuario = User.objects.get(pk = user.id)
        persona = Persona.objects.get(usuario_id=user.id)
        usuario.first_name= form.cleaned_data['first_name']
        usuario.last_name= form.cleaned_data['last_name']
        usuario.email = form.cleaned_data['email']
        persona.telefono = form.cleaned_data['telefono']
        usuario.save()
        persona.save()
        return super(CuentaEditarView, self).form_valid(form)

def contrasena_editar(request, template_name='main/contrasena-editar.html',
                    post_change_redirect=None):
    message = None
    persona = Persona.objects.get(usuario = request.user)
    if persona.tipo_persona == 'R':
        tipo = True
    else:
        tipo = False
    if post_change_redirect is None:
        post_change_redirect = reverse_lazy('homepage')
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(post_change_redirect)
        else:
            message = 'Constraseña invalida'
            form = forms.EditarUsuarioForm(request.user)
    else:
        form = forms.EditarUsuarioForm(request.user)

    return render_to_response(template_name, {
        'form': form ,'message': message, 'tipo': tipo ,
    }, context_instance=RequestContext(request))

def terminos_condiciones(request):
    return render_to_response('main/terminos-condiciones.html',
                              context_instance=RequestContext(request))

def error404 (request):
    return render_to_response('404.html',
                              context_instance=RequestContext(request))

class UniversidadBusquedaView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        busqueda = request.GET['busqueda']
        universidades = Universidad.objects.filter(Q(descripcion__icontains=busqueda))
        data = serializers.serialize('json', universidades,
                                     fields=('id','descripcion','nemonico'))
        return HttpResponse(data, content_type='application/json')

class PaisBusquedaView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        busqueda = request.GET['busqueda']
        paises = Pais.objects.filter(Q(descripcion__icontains=busqueda))
        data = serializers.serialize('json', paises,
                                     fields=('id','descripcion'))
        return HttpResponse(data, content_type='application/json')

class CiudadBusquedaView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        pais = request.GET['pais']
        ciudades = Ciudad.objects.filter(pais_id=pais )
        data = serializers.serialize('json', ciudades,
                                     fields=('id','descripcion'))
        return HttpResponse(data, content_type='application/json')

class CarreraBusquedaPorTipoView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        tipo = request.GET['tipo']
        carreras = Carrera.objects.filter(tipo_carrera_id =tipo )
        data = serializers.serialize('json', carreras,
                                     fields=('id','descripcion'))
        return HttpResponse(data, content_type='application/json')

class CarreraBusquedaView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        busqueda = request.GET['busqueda']
        carreras = Carrera.objects.filter(Q(descripcion__icontains=busqueda))
        data = serializers.serialize('json', carreras,
                                     fields=('id','descripcion'))
        return HttpResponse(data, content_type='application/json')

class PeriodosGraduacionBusquedaView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        tipo = request.GET['tipo']
        tipo_carrera = TipoCarrera.objects.get(id = tipo)
        if  tipo_carrera.id == 1:
            listado_periodo = PeriodosGraduacion.objects.filter()

            l_periodo =[]

            for periodo in listado_periodo:
                e = {
                    "id": periodo.id,
                    "descripcion": periodo.descripcion,
                    "secuencia": periodo.secuencia_universitaria
                }
                l_periodo.append(e)
            data = json.dumps(l_periodo)
            # data = serializers.serialize('json', carreras,
            #                          fields=('id','descripcion', 'secuencia_universitaria'))
        else:
            listado_periodo = PeriodosGraduacion.objects.filter(secuencia_tecnica__isnull=False)
            l_periodo =[]

            for periodo in listado_periodo:
                e = {
                    "id": periodo.id,
                    "descripcion": periodo.descripcion,
                    "secuencia": periodo.secuencia_tecnica
                }
                l_periodo.append(e)
            data = json.dumps(l_periodo)
            # data = serializers.serialize('json', carreras,
            #                          fields=('id','descripcion', 'secuencia_tecnica'))

        return HttpResponse(data, content_type='application/json')




