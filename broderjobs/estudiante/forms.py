# coding=utf-8
from django import forms
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from django.forms import RadioSelect, Select, CheckboxSelectMultiple
from .models import ExperienciaProfesional, Voluntariado, ActividadesExtra, Estudiante
from models import Persona, GradoEstudio, Universidad, Carrera, Pais, Ciudad, TipoPuesto, CargaHoraria,Idioma, Conocimiento
from empresa.models import EvaluacionEmpresa, Puesto, Empresa
from main import utilitarios

class RegistroCVForm(forms.ModelForm):

    universidades = forms.CharField(required = True,  max_length = 50, widget=forms.TextInput(attrs={'placeholder': 'Universidades', 'class': 'full'}))
    universidades_hidden = forms.CharField(widget=forms.HiddenInput())

    carreras = forms.CharField(required = True,  max_length = 50, widget=forms.TextInput(attrs={'placeholder': 'Carreras', 'class': 'full'}))
    carreras_hidden = forms.CharField(widget=forms.HiddenInput())

    paises = forms.CharField(required = True,  max_length = 50, widget=forms.TextInput(attrs={'placeholder': 'Pais', 'class': 'full'}))
    paises_hidden = forms.CharField(widget=forms.HiddenInput())

    ciudades = forms.CharField(required = True,  max_length = 50, widget=forms.TextInput(attrs={'placeholder': 'Ciudad', 'class': 'full'}))
    ciudades_hidden = forms.CharField(widget=forms.HiddenInput())

    class Meta:
            model = Estudiante
            fields = ('grado_estudio', 'semestre_inicio_estudio', 'ano_inicio_estudio', 'semestre_graduacion',
                     'ano_graduacion', 'tipo_puesto', 'carga_horaria')
            widgets = {
                'grado_estudio': Select(attrs={'class': 'full'}),
                'tipo_puesto': CheckboxSelectMultiple(),
                'carga_horaria': RadioSelect(),
            }

    def __init__(self, *args, **kwargs):
        super(RegistroCVForm, self).__init__(*args, **kwargs)
        self.fields['grado_estudio'].empty_label = 'Seleccione'
        self.fields['carga_horaria'].empty_label = None

        #Carga items Semestre
        items_semestre = utilitarios.semestre_rango()
        self.fields['semestre_inicio_estudio'].widget = forms.Select(attrs={'class': 'half-medio'})
        self.fields['semestre_graduacion'].widget = forms.Select(attrs={'class': 'half-medio'})

        self.fields['semestre_inicio_estudio'].choices = items_semestre
        self.fields['semestre_graduacion'].choices = items_semestre

        #Carga items a aÃ±os

        items_anos = utilitarios.anos_rango()
        self.fields['ano_inicio_estudio'].widget = forms.Select(attrs={'class': 'half-medio'})
        self.fields['ano_inicio_estudio'].choices = items_anos

        self.fields['ano_graduacion'].widget = forms.Select(attrs={'class': 'half-medio'})
        self.fields['ano_graduacion'].choices = items_anos

class FotoForm(forms.Form):

   foto = forms.ImageField(required=False, error_messages = {'invalid':'Porfavor seleccione una Imagen valida'}, widget=forms.FileInput)

class UniqueUserEmailField(forms.EmailField):
    def validate(self, value):
        super(forms.EmailField, self).validate(value)
        try:
            User.objects.get(email = value)
            raise forms.ValidationError("Email ya esta registrado")
        except User.MultipleObjectsReturned:
            raise forms.ValidationError("Email ya esta registrado")
        except User.DoesNotExist:
            pass

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ('grado_estudio', 'universidad', 'carrera', 'semestre_inicio_estudio', 'ano_inicio_estudio',
                  'semestre_graduacion', 'ano_graduacion', 'ciudad', 'pais')
    @property
    def helper(self):
        helper = FormHelper()
        helper.form_tag = False # don't render form DOM element
        helper.render_unmentioned_fields = True # render all fields
        return helper

class InfoPersonalForm(EstudianteForm):
    email = forms.CharField(required = True,  max_length = 50, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    fecha_nacimiento = forms.DateField(required=False, input_formats=['%Y-%m-%d'])
    telefono = forms.CharField(required = False, max_length = 20, widget=forms.TextInput(attrs={'placeholder': 'Celular'}))

    @property
    def helper(self):
        helper = FormHelper()
        helper.form_tag = False # don't render form DOM element
        helper.render_unmentioned_fields = True # render all fields
        return helper

class ResumenForm(forms.Form):
    resumen = forms.CharField(required=True, widget=forms.Textarea)

    @property
    def helper(self):
        helper = FormHelper()
        helper.form_tag = False # don't render form DOM element
        helper.render_unmentioned_fields = True # render all fields
        helper.label_class = 'col-md-2'
        helper.field_class = 'col-md-10'
        return helper

class DisponibilidadForm(forms.ModelForm):
    class Meta:
            model = Estudiante
            fields = ('tipo_puesto', 'carga_horaria')
            widgets = {
                'tipo_puesto': forms.widgets.CheckboxSelectMultiple,
                'carga_horaria': forms.widgets.RadioSelect()
            }
    def __init__(self, *args, **kwargs):
        super(DisponibilidadForm, self).__init__(*args, **kwargs)
        self.fields['carga_horaria'].empty_label = None
        self.fields['tipo_puesto'].empty_label = None

    @property
    def helper(self):
        helper = FormHelper()
        helper.form_tag = False # don't render form DOM element
        helper.render_unmentioned_fields = True # render all fields
        return helper

class IdiomaForm(forms.Form):

    idioma = forms.ModelMultipleChoiceField(queryset= Idioma.objects.all(), required = False, widget=forms.SelectMultiple(attrs={'class': 'full'}))

    @property
    def helper(self):
        helper = FormHelper()
        helper.form_tag = False # don't render form DOM element
        helper.render_unmentioned_fields = True # render all fields
        return helper

class ConocimientoForm(forms.Form):


    conocimiento = forms.ModelMultipleChoiceField(queryset=Conocimiento.objects.all(),  required = False, widget=forms.SelectMultiple(attrs={'class': 'full', }))


    @property
    def helper(self):
        helper = FormHelper()
        helper.form_tag = False # don't render form DOM element
        helper.render_unmentioned_fields = True # render all fields
        return helper

class ExperienciaForm(forms.ModelForm):
    fecha_desde = forms.DateField(widget=forms.DateInput())
    fecha_hasta = forms.DateField(required=False, widget=forms.DateInput())

    puestos = forms.CharField(required = True,  max_length = 50, widget=forms.TextInput(attrs={'placeholder': 'Puestos', 'class': 'full'}))
    puestos_hidden = forms.CharField(widget=forms.HiddenInput())

    empresas = forms.CharField(required = True,  max_length = 50, widget=forms.TextInput(attrs={'placeholder': 'Empresas', 'class': 'full'}))
    empresas_hidden = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = ExperienciaProfesional
        fields = ('fecha_desde','fecha_hasta', 'descripcion')
        widget = {
            'descripcion': forms.widgets.Textarea

        }

    @property
    def helper(self):
        helper = FormHelper()
        helper.form_tag = False # don't render form DOM element
        helper.render_unmentioned_fields = True # render all fields
        return helper

class VoluntariadoForm(forms.ModelForm):
    fecha_desde = forms.DateField(required=False, widget=forms.DateInput())
    fecha_hasta = forms.DateField(required=False, widget=forms.DateInput())
    class Meta:
        model = Voluntariado
        fields = ('cargo', 'organizacion', 'fecha_desde','fecha_hasta', 'descripcion')

    @property
    def helper(self):
        helper = FormHelper()
        helper.form_tag = False # don't render form DOM element
        helper.render_unmentioned_fields = True # render all fields
        return helper

class ActividadesExtraForm(forms.ModelForm):
    class Meta:
        model = ActividadesExtra
        fields = ('organizacion', 'descripcion')

    @property
    def helper(self):
        helper = FormHelper()
        helper.form_tag = False # don't render form DOM element
        helper.render_unmentioned_fields = True # render all fields
        return helper

class EvaluacionForm(forms.ModelForm):
    class Meta:
        model = EvaluacionEmpresa
        fields = ('linea_carrera', 'flexibilidad_horarios', 'ambiente_trabajo', 'salarios')
        



