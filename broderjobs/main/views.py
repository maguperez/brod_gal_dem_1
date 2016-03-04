# coding=utf-8
import json
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, HttpResponseRedirect, render
from .forms import RegisterForm, LoginForm, PasswordResetForm, CuentaEditarForm
from django.contrib.auth import authenticate, login, logout
from  django.utils.dateparse import parse_date
from django.contrib.auth.models import User
from django.views.generic import TemplateView,FormView
from django.core.urlresolvers import reverse_lazy, reverse
from .models import Persona, Ciudad, Pais, Carrera, TipoCarrera, PeriodosGraduacion, Universidad
from empresa.models import Representante, Empresa
from main.utils import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.core.context_processors import csrf
from django.core import serializers

from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template import loader
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from broderjobs.settings import DEFAULT_FROM_EMAIL
from django.views.generic import *
from django.contrib import messages
from django.db.models.query_utils import Q


def homepage(request):
    message_registro = None
    message_login = None
    message_reset = None
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
            reset_form = PasswordResetForm(prefix='reset')
        return render_to_response('main/home-estudiante.html', {'message_login': message_login,
                                                                'message_registro': message_registro,
                                                                'message_reset': message_reset,
                                                                'login_form': login_form ,
                                                                'registro_form': registro_form,
                                                                'reset_form': reset_form},
                                      context_instance=RequestContext(request))
    else:
        if request.method == "POST":
            login_form = LoginForm(request.POST, prefix='login')
            registro_form = RegisterForm(request.POST, prefix='registro')
            reset_form = PasswordResetForm(request.POST, prefix='reset')
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
            if '_reset' in request.POST:
                if reset_form.is_valid():
                    data = reset_form.cleaned_data["email_or_username"]
                if validate_email_address(data) is True:                 #uses the method written above
                    associated_users= User.objects.filter(Q(email=data)|Q(username=data))
                    if associated_users.exists():
                        for user in associated_users:
                                c = {
                                    'email': user.email,
                                    'domain': request.META['HTTP_HOST'],
                                    'site_name': 'your site',
                                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                                    'user': user,
                                    'token': default_token_generator.make_token(user),
                                    'protocol': 'http',
                                    }
                                subject_template_name='registration/password_reset_subject.txt'
                                # copied from django/contrib/admin/templates/registration/password_reset_subject.txt to templates directory
                                email_template_name='main/password_reset_email.html'
                                # copied from django/contrib/admin/templates/registration/password_reset_email.html to templates directory
                                subject = loader.render_to_string(subject_template_name, c)
                                # Email subject *must not* contain newlines
                                subject = ''.join(subject.splitlines())
                                email = loader.render_to_string(email_template_name, c)
                                send_mail(subject, email, DEFAULT_FROM_EMAIL , [user.email], fail_silently=False)
                        # result = self.form_valid(form)
                        message_reset= "se ha enviado un correo"# return result
                    else:
                        message_reset = "No pudimos encontrar el correo"# r
                    # return result
                else:
                    message_registro = "No pudimos encontrar el correo"# r
        else:
            login_form = LoginForm(prefix='login')
            registro_form = RegisterForm(prefix='registro')
            reset_form = PasswordResetForm(prefix='reset')

        return render_to_response('main/home-estudiante.html', {'message_login': message_login,
                                                                'message_registro': message_registro,
                                                                'message_reset': message_reset,
                                                                'login_form': login_form ,
                                                                'registro_form': registro_form,
                                                                'reset_form': reset_form},
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
    form_class = CuentaEditarForm
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





def validate_email_address(email):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False
# class ResetPasswordView(FormView):
#         template_name = "account/test_template.html"    #code for template is given below the view's code
#         success_url = '/account/login'
#         form_class = form.PasswordResetForm
#
#         @staticmethod
#         def validate_email_address(email):
#             try:
#                 validate_email(email)
#                 return True
#             except ValidationError:
#                 return False
#
#         def post(self, request, *args, **kwargs):
#             '''
#             A normal post request which takes input from field "email_or_username" (in ResetPasswordRequestForm).
#             '''
#             form = self.form_class(request.POST)
#             if form.is_valid():
#                 data= form.cleaned_data["email_or_username"]
#             if self.validate_email_address(data) is True:                 #uses the method written above
#                 '''
#                 If the input is an valid email address, then the following code will lookup for users associated with that email address. If found then an email will be sent to the address, else an error message will be printed on the screen.
#                 '''
#                 associated_users= User.objects.filter(Q(email=data)|Q(username=data))
#                 if associated_users.exists():
#                     for user in associated_users:
#                             c = {
#                                 'email': user.email,
#                                 'domain': request.META['HTTP_HOST'],
#                                 'site_name': 'your site',
#                                 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                                 'user': user,
#                                 'token': default_token_generator.make_token(user),
#                                 'protocol': 'http',
#                                 }
#                             subject_template_name='registration/password_reset_subject.txt'
#                             # copied from django/contrib/admin/templates/registration/password_reset_subject.txt to templates directory
#                             email_template_name='registration/password_reset_email.html'
#                             # copied from django/contrib/admin/templates/registration/password_reset_email.html to templates directory
#                             subject = loader.render_to_string(subject_template_name, c)
#                             # Email subject *must not* contain newlines
#                             subject = ''.join(subject.splitlines())
#                             email = loader.render_to_string(email_template_name, c)
#                             send_mail(subject, email, DEFAULT_FROM_EMAIL , [user.email], fail_silently=False)
#                     result = self.form_valid(form)
#                     messages.success(request, 'An email has been sent to ' + data +". Please check its inbox to continue reseting password.")
#                     return result
#                 result = self.form_invalid(form)
#                 messages.error(request, 'No user is associated with this email address')
#                 return result
#             else:
#                 '''
#                 If the input is an username, then the following code will lookup for users associated with that user. If found then an email will be sent to the user's address, else an error message will be printed on the screen.
#                 '''
#                 associated_users= User.objects.filter(username=data)
#                 if associated_users.exists():
#                     for user in associated_users:
#                         c = {
#                             'email': user.email,
#                             'domain': 'example.com', #or your domain
#                             'site_name': 'example',
#                             'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                             'user': user,
#                             'token': default_token_generator.make_token(user),
#                             'protocol': 'http',
#                             }
#                         subject_template_name='registration/password_reset_subject.txt'
#                         email_template_name='registration/password_reset_email.html'
#                         subject = loader.render_to_string(subject_template_name, c)
#                         # Email subject *must not* contain newlines
#                         subject = ''.join(subject.splitlines())
#                         email = loader.render_to_string(email_template_name, c)
#                         send_mail(subject, email, DEFAULT_FROM_EMAIL , [user.email], fail_silently=False)
#                     result = self.form_valid(form)
#                     messages.success(request, 'Email has been sent to ' + data +"'s email address. Please check its inbox to continue reseting password.")
#                     return result
#                 result = self.form_invalid(form)
#                 messages.error(request, 'This username does not exist in the system.')
#                 return result
#             messages.error(request, 'Invalid Input')
#             return self.form_invalid(form)




