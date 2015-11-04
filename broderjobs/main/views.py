from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, HttpResponseRedirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout

from django.views.generic import TemplateView,FormView
from django.core.urlresolvers import reverse_lazy
from .models import Persona
from django.core.context_processors import csrf


class EstudianteResgistro(FormView):
    template_name = 'main/estudiante_registro.html'
    form_class = RegisterForm
    success_url = reverse_lazy('registrocv')

    def form_valid(self, form):
        user = form.save()
        persona = Persona()
        persona.usuario = user
        persona.fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
        persona.tipo_persona = "E"
        persona.save()
        return super(EstudianteResgistro, self).form_valid(form)

class EmpresaRegistro(FormView):
    template_name = 'main/empresa_registro.html'
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
                    return redirect('homepage')
                else:
                    message = "tu usuario esta inactivo"
            else:
                message = "Email o contraea incorrecta"
    else:
        form = LoginForm()

    return render_to_response('main/estudiante_login.html',{'message': message,'form': form},
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

    return render_to_response('main/empresa_login.html',{'message': message,'form': form},
                                  context_instance=RequestContext(request))

def homepage(request):
    return render_to_response('main/estudiante.html',
                              context_instance=RequestContext(request))
def estudiante(request):
    return render_to_response('main/estudiante.html',
                              context_instance=RequestContext(request))
def empresa(request):
    return render_to_response('main/index_empresa.html',
                              context_instance=RequestContext(request))
def logout_view(request):
    logout(request)
    return redirect('homepage')

def register_user(request):
    message = None
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            persona = Persona()
            persona.usuario = user
            persona.fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            persona.tipo_persona = "E"
            persona.save()
            return reverse_lazy('registrocv')
    form = RegisterForm()
    message = "esta mierda"
    return render_to_response('main/estudiante_registro.html', {'message': message,'form': form}, context_instance=RequestContext(request))


