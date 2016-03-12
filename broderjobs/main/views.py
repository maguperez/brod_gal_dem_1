# coding=utf-8
import json
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, HttpResponseRedirect, render, get_object_or_404
from .forms import RegisterForm, LoginForm, CuentaEditarForm, CuentaCrearForm, EditarUsuarioForm
from django.contrib.auth import authenticate, login, logout
from  django.utils.dateparse import parse_date
from django.contrib.auth.models import User
from django.views.generic import TemplateView,FormView
from django.core.urlresolvers import reverse_lazy, reverse
from .models import Persona, Ciudad, Pais, Carrera, TipoCarrera, PeriodosGraduacion, Universidad
from estudiante.models import Estudiante
from empresa.models import Representante, Empresa
from main.utils import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, PasswordResetForm
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

from django.shortcuts import redirect
from django.views.generic import CreateView
from .models import User

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

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
                    estudiante = Estudiante()
                    estudiante.persona = persona
                    estudiante.save()
                    new_user = authenticate(username=request.POST['registro-email'],
                                            password=request.POST['registro-password1'])
                    login(request, new_user)
                    return redirect('registro-cv')
                else:
                    message_registro= "El email ya ha sido  registrado"
            if '_reset' in request.POST:
                data = None
                if reset_form.is_valid():
                    data = reset_form.cleaned_data["email"]
                if validate_email_address(data) is True:                 #uses the method written above
                    associated_users= User.objects.filter(Q(email=data)|Q(username=data))
                    if associated_users.exists():
                        for user in associated_users:
                            # opts = {
                            #     'use_https': request.is_secure(),
                            #     'email_template_name': 'correos/OlvidoContrasena.html',
                            #     'subject_template_name': 'correos/OlvidoContrasenaSubject.txt',
                            #     'request': request,
                            #     # 'html_email_template_name': provide an HTML content template if you desire.
                            # }
                            # This form sends the email on save()
                            # reset_form.save(**opts)
                            # c = {
                            #     'email': user.email,
                            #     'domain': request.META['HTTP_HOST'],
                            #     'site_name': 'your site',
                            #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                            #     'user': user,
                            #     'token': default_token_generator.make_token(user),
                            #     'protocol': 'http',
                            # }
                            #
                            # subject_template_name='correos/OlvidoContrasenaSubject.txt'
                            # email_template_name='correos/OlvidoContrasena.html'
                            # subject = loader.render_to_string(subject_template_name, c)
                            # subject = ''.join(subject.splitlines())
                            # email = loader.render_to_string(email_template_name, c)
                            # send_mail(subject, email, DEFAULT_FROM_EMAIL , [user.email], fail_silently=False)
                            # result = reset_form(form)
                            plaintext = get_template('correos/OlvidoContrasenaSubject.txt')
                            htmly     = get_template('correos/OlvidoContrasena.html')
                            d = Context({ 'nombre': user.first_name, 'email': user.email,
                                          'domain': request.META['HTTP_HOST'],
                                          'site_name': 'your site',
                                          'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                                          'user': user,
                                          'token': default_token_generator.make_token(user),
                                          'protocol': 'http'
                                          })
                            subject, from_email, to = 'Recuperar Contraseña', DEFAULT_FROM_EMAIL, user.email
                            text_content = plaintext.render(d)
                            html_content = htmly.render(d)
                            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                            msg.attach_alternative(html_content, "text/html")
                            msg.send()
                        message_reset= "se ha enviado un correo"
                    else:
                        message_reset = "No pudimos encontrar el correo"
                    # return result
                else:
                    message_registro = "No pudimos encontrar el correo"
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
    message_login = None
    message_registro = None
    message_reset = None
    if request.user.is_authenticated():
        return redirect('empresa-oportunidad-listar')
    else:
        if request.method == "POST":
            login_form = LoginForm(request.POST, prefix='login')
            registro_form = RegisterForm(request.POST, prefix='registro')
            reset_form = PasswordResetForm(request.POST, prefix='reset')
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
                            if user.is_active and persona.estado == 'A':
                                login(request, user)
                                return redirect('empresa-oportunidad-listar')
                            else:
                                message_login = "Tu usuario esta siendo validado pronto nos comunicaremos contigo"
                    else:
                        message_login = "Email o contraseña incorrecta"
            if '_registro' in request.POST:
                if registro_form.is_valid():
                    user = registro_form.save()
                    persona = Persona()
                    persona.usuario = user
                    persona.tipo_persona = "R"
                    persona.telefono = registro_form.cleaned_data['telefono']
                    persona.estado= 'I'
                    empresa = registro_form.cleaned_data['empresa']
                    persona.save()
                    representante = Representante()
                    representante.persona = persona
                    representante.empresa = empresa
                    representante.save()
                    # new_user = authenticate(username=request.POST['registro-email'], password=request.POST['registro-password1'])
                    # login(request, new_user)

                    ## Mensaje a Usuario Nuevo
                    plaintext = get_template('correos/CuentaRegistroEmpresaSubject.txt')
                    htmly     = get_template('correos/CuentaRegistroEmpresa.html')
                    d = Context({ 'nombre': user.first_name, 'email': user.email,
                                  'domain': request.META['HTTP_HOST'],
                                  'site_name': 'your site',
                                  'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                                  'user': user,
                                  'token': default_token_generator.make_token(user),
                                  'protocol': 'http'
                                })
                    subject, from_email, to = 'Registro en BroderJobs', DEFAULT_FROM_EMAIL, user.email
                    text_content = plaintext.render(d)
                    html_content = htmly.render(d)
                    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()

                    # Envio de mensaje a info
                    plaintext = get_template('correos/AvisoRegistroEmpresaSubject.txt')
                    htmly     = get_template('correos/AvisoRegistroEmpresa.html')
                    d = Context({ 'nombre': user.first_name, 'email': user.email,
                                  'domain': request.META['HTTP_HOST'],
                                  'site_name': 'your site',
                                  'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                                  'user': user,
                                  'persona': persona,
                                  'representante': representante,
                                  'token': default_token_generator.make_token(user),
                                  'protocol': 'http'
                                })
                    subject, from_email, to = 'Nuevo Registro en Empresas', DEFAULT_FROM_EMAIL, DEFAULT_FROM_EMAIL
                    text_content = plaintext.render(d)
                    html_content = htmly.render(d)
                    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()

                    # # Envio de Mensaje a Broder INfo
                    # datos = {
                    #     'persona': user.first_name + ' ' + user.last_name,
                    #     'empresa': representante.empresa,
                    #     'email': user.email,
                    #     'telefono': persona.telefono
                    # }
                    # email_template_name='correos/AvisoRegistroEmpresa.html'
                    # subject = 'correos/AvisoRegistroEmpresaSubject.txt'
                    # email = loader.render_to_string(email_template_name, datos)
                    # send_mail(subject, email, DEFAULT_FROM_EMAIL , [DEFAULT_FROM_EMAIL], fail_silently=False)

                    # #Envio de mensaje a Representante
                    # email_template_name='correos/CuentaRegistroEmpresa.html'
                    # subject = 'correos/CuentaRegistroEmpresaSubject.txt'
                    # email = loader.render_to_string(email_template_name, datos)
                    # send_mail(subject, email, DEFAULT_FROM_EMAIL , [user.email], fail_silently=False)

                    message_registro = "Tu usuario esta siendo validado pronto nos comunicaremos contigo"
                else:
                    message_registro= "El email ya ha sido  registrado"

            if '_reset' in request.POST:
                data = None
                if reset_form.is_valid():
                    data = reset_form.cleaned_data["email"]
                if validate_email_address(data) is True:                 #uses the method written above
                    associated_users= User.objects.filter(Q(email=data)|Q(username=data))
                    if associated_users.exists():
                        for user in associated_users:
                            # opts = {
                            #     'use_https': request.is_secure(),
                            #     'email_template_name': 'correos/OlvidoContrasena.html',
                            #     'subject_template_name': 'correos/OlvidoContrasenaSubject.txt',
                            #     'request': request,
                            # }
                            plaintext = get_template('correos/OlvidoContrasenaSubject.txt')
                            htmly     = get_template('correos/OlvidoContrasena.html')
                            d = Context({ 'nombre': user.first_name, 'email': user.email,
                                          'domain': request.META['HTTP_HOST'],
                                          'site_name': 'your site',
                                          'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                                          'user': user,
                                          'token': default_token_generator.make_token(user),
                                          'protocol': 'http'
                                          })
                            subject, from_email, to = 'Recuperar Contraseña', DEFAULT_FROM_EMAIL, user.email
                            text_content = plaintext.render(d)
                            html_content = htmly.render(d)
                            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                            msg.attach_alternative(html_content, "text/html")
                            msg.send()
                            reset_form.save(**opts)
                        message_reset= "se ha enviado un correo"
                    else:
                        message_reset = "No pudimos encontrar el correo"
                    # return result
                else:
                    message_registro = "No pudimos encontrar el correo"
            else:
                login_form = LoginForm(prefix='login')
                registro_form = RegisterForm(prefix='registro')
                reset_form = PasswordResetForm(prefix='reset')

            return render_to_response('main/home-empresa.html', {'message_login': message_login,
                                                                'message_registro': message_registro,
                                                                'message_reset': message_reset,
                                                                'login_form': login_form ,
                                                                'registro_form': registro_form,
                                                                'reset_form': reset_form},
                                    context_instance=RequestContext(request))
        else:
            login_form = LoginForm(prefix='login')
            registro_form = RegisterForm(prefix='registro')
            reset_form = PasswordResetForm(prefix='reset')
            return render_to_response('main/home-empresa.html', {'message_login': message_login,
                                                                'message_registro': message_registro,
                                                                'message_reset': message_reset,
                                                                'login_form': login_form ,
                                                                'registro_form': registro_form,
                                                                'reset_form': reset_form},
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
        context['tipo'] = tipo
        context['administrador'] = representante.administrador
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
        representante = Representante()
        if persona.tipo_persona == 'R':
            representante = get_object_or_404(Representante, persona_id = persona.id)
            tipo = True
        else:
            tipo = False
        context = super(CuentaEditarView, self).get_context_data(**kwargs)
        context['tipo'] = tipo
        context['representante'] = representante
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

class CuentaCrearView(LoginRequiredMixin, FormView):
    template_name = 'main/cuenta-crear.html'
    form_class = CuentaCrearForm
    success_url = reverse_lazy('usuarios')
    model = User
    template_name = 'main/cuenta-crear.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        persona = Persona.objects.get(usuario_id=user.id)
        if persona.tipo_persona == 'R':
            tipo = True
        else:
            tipo = False
        context = super(CuentaCrearView, self).get_context_data(**kwargs)
        context['tipo'] = tipo
        return context

    def form_valid(self, form):
        representante_actual = get_object_or_404(Representante, persona__usuario_id = self.request.user.id)
        usuario = form.save(commit=False)
        usuario.username = generate_username(form.cleaned_data['email'])
        usuario.first_name = form.cleaned_data['first_name']
        usuario.last_name= form.cleaned_data['last_name']
        usuario.set_password(User.objects.make_random_password())
        usuario.save()
        persona = Persona()
        persona.usuario = usuario
        persona.tipo_persona = "R"
        # persona.telefono = registro_form.cleaned_data['telefono']
        persona.save()
        empresa = representante_actual.empresa
        representante = Representante()
        representante.persona = persona
        representante.empresa = empresa
        representante.save()

        # This form only requires the "email" field, so will validate.
        reset_form = PasswordResetForm(self.request.POST)
        reset_form.is_valid()  # Must trigger validation
        # Copied from django/contrib/auth/views.py : password_reset
        # opts = {
        #     'use_https': self.request.is_secure(),
        #     'email_template_name': 'correos/CuentaCreada.html',
        #     'subject_template_name': 'correos/CuentaCreadaSubject.txt',
        #     'request': self.request,
        #     # 'html_email_template_name': provide an HTML content template if you desire.
        # }
        # # This form sends the email on save()
        # reset_form.save(**opts)
        plaintext = get_template('correos/CuentaCreadaSubject.txt')
        htmly     = get_template('correos/CuentaCreada.html')
        d = Context({ 'nombre': usuario.first_name, 'email': usuario.email,
                      'domain': self.request.META['HTTP_HOST'],
                      'site_name': 'your site',
                      'uid': urlsafe_base64_encode(force_bytes(usuario.pk)),
                      'user': usuario,
                      'token': default_token_generator.make_token(usuario),
                      'protocol': 'http'
                    })
        subject, from_email, to = 'Recuperar Contraseña', DEFAULT_FROM_EMAIL, usuario.email
        text_content = plaintext.render(d)
        html_content = htmly.render(d)
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return super(CuentaCrearView, self).form_valid(form)
        # return redirect('usuarios')

def generate_username(email):
    # TODO: Something more efficient?
    highest_user_id = User.objects.all().order_by('-id')[0].id
    leading_part_of_email = email.split('@',1)[0]
    # leading_part_of_email = re.sub(r'[^a-zA-Z0-9+]', '',
    #                               leading_part_of_email)
    truncated_part_of_email = leading_part_of_email[:3]+ leading_part_of_email[-3:]
    derived_username = truncated_part_of_email + str(highest_user_id+1)
    return derived_username

# def contrasena_crear(request):
#     message = None
#     if request.method == "POST":
#         form = PasswordResetForm(request.user, request.POST)
#         if form.is_valid():
#             form.save()
#             return render_to_response('main/contrasena-crear.html', {'message': message,'form': form},
#                                       context_instance=RequestContext(request))
#         else:
#             message = 'Constraseña invalida'
#             # form = EditarUsuarioForm(request.user)
#     # else:
#     #     form = EditarUsuarioForm(request.user)
#     return render_to_response('main/contrasena-crear.html', {'message': message,'form': form},
#                               context_instance=RequestContext(request))

def contrasena_crear(request, password_reset_form=PasswordResetForm, token_generator=default_token_generator, post_reset_redirect=None):
    message = None
    if request.method == "POST":
        form = PasswordResetForm(request.user, request.POST)
        usuario = get_object_or_404(User, pk = request.user.id)
        if form.is_valid():
            form.save()
            login(request, usuario)
            return redirect('empresa-oportunidad-listar')
        else:
            message = 'Constraseña invalida'
            form = PasswordResetForm(request.user)
    else:
        form = PasswordResetForm(request.user)

    return render_to_response('main/contrasena-crear.html', {
        'form': form ,'message': message,
    }, context_instance=RequestContext(request))

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
            form = EditarUsuarioForm(request.user)
    else:
        form = EditarUsuarioForm(request.user)

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

###################################################################################
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template import loader
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from broderjobs.settings import DEFAULT_FROM_EMAIL
from django.views.generic import *


class ResetPasswordRequestView(FormView):
    template_name = "registration/template_reset.html"    #code for template is given below the view's code
    success_url = ''
    form_class = PasswordResetForm

    @staticmethod
    def validate_email_address(email):

        try:
            validate_email(email)
            return True
        except ValidationError:
            return False

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            data= form.cleaned_data["email_or_username"]
        if self.validate_email_address(data) is True:
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
                        'protocol': 'http',}

                    subject_template_name='registration/password_reset_subject.txt'
                    # copied from django/contrib/admin/templates/registration/password_reset_subject.txt to templates directory
                    email_template_name='registration/password_reset_email.html'
                    # copied from django/contrib/admin/templates/registration/password_reset_email.html to templates directory
                    subject = loader.render_to_string(subject_template_name, c)
                    # Email subject *must not* contain newlines
                    subject = ''.join(subject.splitlines())
                    email = loader.render_to_string(email_template_name, c)
                    send_mail(subject, email, DEFAULT_FROM_EMAIL , [user.email], fail_silently=False)
                result = self.form_valid(form)
                messages.success(request, 'An email has been sent to ' + data +". Please check its inbox to continue reseting password.")
                return result
            result = self.form_invalid(form)
            messages.error(request, 'No user is associated with this email address')
            return result
        else:
            associated_users= User.objects.filter(username=data)
            if associated_users.exists():
                for user in associated_users:
                    c = {
                        'email': user.email,
                        'domain': 'example.com', #or your domain
                        'site_name': 'example',
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'user': user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    subject_template_name='registration/password_reset_subject.txt'
                    email_template_name='registration/password_reset_email.html'
                    subject = loader.render_to_string(subject_template_name, c)
                    # Email subject *must not* contain newlines
                    subject = ''.join(subject.splitlines())
                    email = loader.render_to_string(email_template_name, c)
                    send_mail(subject, email, DEFAULT_FROM_EMAIL , [user.email], fail_silently=False)
                result = self.form_valid(form)
                messages.success(request, 'Email has been sent to ' + data +"'s email address. Please check its inbox to continue reseting password.")
                return result
                result = self.form_invalid(form)
            messages.error(request, 'This username does not exist in the system.')
            return result
        messages.error(request, 'Invalid Input')
        return self.form_invalid(form)





