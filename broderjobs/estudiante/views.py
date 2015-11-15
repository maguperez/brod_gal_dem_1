
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response, redirect
from django.contrib.messages.views import SuccessMessageMixin
from .forms import RegistroCVForm, ResumenForm, FotoForm, InfoPersonalForm
from django.views.generic import TemplateView, FormView
from django.core.urlresolvers import reverse_lazy
from .models import Estudiante, Resumen, EstudianteIdioma, EstudianteConocimiento, ActividadesExtra, ExperienciaProfesional, Voluntariado
from models import Persona, GradoEstudio, Universidad, Carrera, Pais, Ciudad, TipoPuesto
from main import utilitarios


@login_required(login_url='/estudiante-registro/')
def registro_cv(request):

    if request.method == 'POST':
        form = RegistroCVForm(request.POST)
        if form.is_valid():
            user = request.user
            persona = Persona.objects.get(usuario_id=user.id)
            grado_estudio = form.cleaned_data['grado_estudio']
            universidad = form.cleaned_data['universidad']
            carrera = form.cleaned_data['carrera']
            pais =  form.cleaned_data['pais']
            ciudad = form.cleaned_data['ciudad']
            tipo_puesto = form.cleaned_data['tipo_puesto']
            ano_inicio = form.cleaned_data['ano_inicio_estudio']
            semestre_inicio = form.cleaned_data['semestre_inicio_estudio']
            ano_graduacion = form.cleaned_data['ano_graduacion']
            semestre_graduacion = form.cleaned_data['semestre_graduacion']

            estudiante = Estudiante()
            estudiante.persona = persona
            estudiante.grado_estudio = grado_estudio
            estudiante.universidad = universidad
            estudiante.carrera = carrera
            estudiante.pais = pais
            estudiante.ciudad = ciudad
            estudiante.ano_inicio_estudio = ano_inicio
            estudiante.semestre_inicio_estudio = semestre_inicio
            estudiante.ano_graduacion = ano_graduacion
            estudiante.semestre_graduacion = semestre_graduacion
            estudiante.save()

            estudiante.tipo_puesto = tipo_puesto
            estudiante.save()

            resumen = Resumen()
            resumen.estudiante = estudiante
            resumen.save()

            return redirect('oportunidad_listar')
    else:
        form = RegistroCVForm()
    return render(request, 'estudiante/registro-cv.html', {'form': form})

@login_required(login_url='/estudiante-registro/')
def oportunidad_listar(request):
    return render(request, 'estudiante/oportunidad-listar.html')

class MiCVView(TemplateView):

    template_name = 'estudiante/mi-cv.html'
    def get_context_data(self, **kwargs):
        user = self.request.user
        persona = Persona.objects.get(usuario_id=user.id)
        estudiante = Estudiante.objects.get(persona_id=persona.id)
        edad = utilitarios.calular_edad(persona.fecha_nacimiento)

        context = super(MiCVView, self).get_context_data(**kwargs)
        context['usuario'] = user
        context['persona'] = persona
        context['estudiante'] = estudiante
        context['edad'] = edad
        context['resumen'] = Resumen.objects.get(estudiante_id=estudiante.id)
        context['idiomas'] = EstudianteIdioma.objects.filter(estudiante_id=estudiante.id)
        context['conocimientos'] = EstudianteConocimiento.objects.filter(estudiante_id=estudiante.id)
        context['actividades_extra'] = ActividadesExtra.objects.filter(estudiante_id=estudiante.id)
        context['experiencias_profesionales'] = ExperienciaProfesional.objects.filter(estudiante_id=estudiante.id)
        context['voluntariados'] = Voluntariado.objects.filter(estudiante_id=estudiante.id)
        return context

class AjaxTemplateMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not hasattr(self, 'ajax_template_name'):
            split = self.template_name.split('.html')
            #split[-1] = '-inner'
            split.append('.html')
            self.ajax_template_name = ''.join(split)
            if request.is_ajax():
                self.template_name = self.ajax_template_name
            return super(AjaxTemplateMixin, self).dispatch(request, *args, **kwargs)

class FotoView(SuccessMessageMixin, AjaxTemplateMixin, FormView):
    template_name = 'estudiante/mi-cv-foto.html'
    form_class = FotoForm
    success_url = reverse_lazy('mi_cv')
    success_message = "Guardado con exito!"

    def get_initial(self):
        user = self.request.user
        persona = Persona.objects.get(usuario_id=user.id)
        estudiante = Estudiante.objects.get(persona_id=persona.id)
        return {'foto': estudiante.foto}

    def form_valid(self, form):
        user = self.request.user
        persona = Persona.objects.get(usuario_id=user.id)
        estudiante = Estudiante.objects.get(persona_id=persona.id)
        estudiante.foto = form.cleaned_data['foto']
        print(estudiante.foto)
        estudiante.save()
        return super(FotoView, self).form_valid(form)

class InfoPersonalView(SuccessMessageMixin, AjaxTemplateMixin, FormView):
    print("ssssssssssssssssssssssssssssssssssssssssssssxxxxxx")
    template_name = 'estudiante/mi-cv-info-personal.html'
    form_class = InfoPersonalForm
    success_url = reverse_lazy('mi_cv')
    success_message = "Guardado con exito!"

    def get_initial(self):
        user = self.request.user
        usuario = User.objects.get(usuario_id =)
        persona = Persona.objects.get(usuario_id=user.id)
        estudiante = Estudiante.objects.get(persona_id=persona.id)
        edad = utilitarios.calular_edad(persona.fecha_nacimiento)
        return {'ano_graduacion' : estudiante.grado_estudio,
                'semestre_graduacion': estudiante.ano_graduacion,
                'email': user.}

    def form_valid(self, form):
        user = self.request.user
        persona = Persona.objects.get(usuario_id=user.id)
        estudiante = Estudiante.objects.get(persona_id=persona.id)
        #estudiante.grado_estudio = form.cleaned_data['grado_estudio']
        #estudiante.universidad = form.cleaned_data['universidad']
        #estudiante.carrera = form.cleaned_data['carrera']
        estudiante.pais =  form.cleaned_data['pais']
        estudiante.ciudad = form.cleaned_data['ciudad']
        #estudiante.ano_inicio = form.cleaned_data['ano_inicio_estudio']
        #estudiante.semestre_inicio = form.cleaned_data['semestre_inicio_estudio']
        estudiante.ano_graduacion = form.cleaned_data['ano_graduacion']
        estudiante.semestre_graduacion = form.cleaned_data['semestre_graduacion']
        persona.email = form.cleaned_data['email']
        persona.save()
        estudiante.save()
        return super(InfoPersonalView, self).form_valid(form)

class ResumenView(SuccessMessageMixin, AjaxTemplateMixin, FormView):
    template_name = 'estudiante/mi-cv-resumen.html'
    form_class = ResumenForm
    success_url = reverse_lazy('mi_cv')
    success_message = "Guardado con exito!"

    def get_initial(self):
        user = self.request.user
        persona = Persona.objects.get(usuario_id=user.id)
        estudiante = Estudiante.objects.get(persona_id=persona.id)
        resumen = Resumen.objects.get(estudiante_id=estudiante.id)
        return {'resumen': resumen.descripcion}

    def form_valid(self, form):
        user = self.request.user
        persona = Persona.objects.get(usuario_id=user.id)
        estudiante = Estudiante.objects.get(persona_id=persona.id)
        resumen = Resumen.objects.get(estudiante_id=estudiante.id)
        resumen.descripcion = form.cleaned_data['resumen']

        resumen.save()
        return super(ResumenView, self).form_valid(form)


