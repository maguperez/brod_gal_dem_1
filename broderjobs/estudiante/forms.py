# coding=utf-8
from django import forms
from django.contrib.auth.models import User
from django.forms import RadioSelect, Select, CheckboxSelectMultiple, TextInput
from docutils.parsers.rst.directives import choice
from .models import ExperienciaProfesional, Voluntariado, ActividadesExtra, Estudiante
from models import Persona, GradoEstudio, Universidad, Carrera, Pais, Ciudad, TipoPuesto, CargaHoraria,Idioma, Conocimiento
from empresa.models import EvaluacionEmpresa, Puesto, Empresa
from main import utils

class RegistroCVForm(forms.ModelForm):
    genero = utils.genero()

    universidades = forms.CharField(required = True,  max_length = 50, widget=forms.TextInput(attrs={'placeholder': 'Selecciona una Universidad', 'class': 'form-control'}))
    universidades_hidden = forms.CharField(widget=forms.HiddenInput())

    carreras = forms.CharField(required = True,  max_length = 50, widget=forms.TextInput(attrs={'placeholder': 'Selecciona una Carrera', 'class': 'form-control'}))
    carreras_hidden = forms.CharField(widget=forms.HiddenInput())
    genero = forms.ChoiceField(choices=genero, required = False, widget=forms.RadioSelect())
    pais = forms.ModelChoiceField(queryset=Pais.objects.all(), empty_label="Seleccione País", required = False, widget=forms.Select(attrs={'class': 'form-control', }))
    ciudad_hidden = forms.CharField(widget=forms.HiddenInput())

    class Meta:
            model = Estudiante
            fields = ('grado_estudio', 'semestre_inicio_estudio', 'ano_inicio_estudio', 'semestre_graduacion',
                     'ano_graduacion', 'tipo_puesto', 'carga_horaria', 'semestre_actual')
            widgets = {
                'grado_estudio': Select(attrs={'class': 'form-control'}),
                'tipo_puesto': CheckboxSelectMultiple(),
                'carga_horaria': RadioSelect(),
                'semestre_actual': Select(attrs={'class': 'form-control'}),
            }

    def __init__(self, *args, **kwargs):
        super(RegistroCVForm, self).__init__(*args, **kwargs)
        self.fields['grado_estudio'].empty_label = 'Seleccione'
        self.fields['carga_horaria'].empty_label = None

        #Carga items Semestre
        items_semestre = utils.semestre_rango()
        self.fields['semestre_inicio_estudio'].widget = forms.Select(attrs={'class': 'form-control'})
        self.fields['semestre_graduacion'].widget = forms.Select(attrs={'class': 'form-control'})

        self.fields['semestre_inicio_estudio'].choices = items_semestre
        self.fields['semestre_graduacion'].choices = items_semestre

        #Carga items a aÃ±os

        items_anos = utils.anos_rango()
        self.fields['ano_inicio_estudio'].widget = forms.Select(attrs={'class': 'form-control'})
        self.fields['ano_inicio_estudio'].choices = items_anos

        self.fields['ano_graduacion'].widget = forms.Select(attrs={'class': 'form-control'})
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
        fields = ('grado_estudio', 'semestre_inicio_estudio', 'ano_inicio_estudio',
                  'semestre_graduacion', 'ano_graduacion','remuneracion', 'semestre_actual')
        widgets = {
                'remuneracion': TextInput(attrs={'class': 'form-control'}),
                'semestre_actual': Select(attrs={'class': 'form-control'}),

            }

class InfoPersonalForm(EstudianteForm):
    genero = utils.genero()

    email = forms.CharField(required = True,  max_length = 50, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    fecha_nacimiento = forms.DateField(required=False, input_formats=['%d/%m/%Y'])

    telefono = forms.CharField(required = False, max_length = 20, widget=forms.TextInput(attrs={'placeholder': 'Celular'}))

    universidades = forms.CharField(required = True,  max_length = 50, widget=forms.TextInput(attrs={'placeholder': 'Universidades', 'class': 'full'}))
    universidades_hidden = forms.CharField(widget=forms.HiddenInput())

    carreras = forms.CharField(required = True,  max_length = 50, widget=forms.TextInput(attrs={'placeholder': 'Carreras', 'class': 'full'}))
    carreras_hidden = forms.CharField(widget=forms.HiddenInput())

    pais = forms.ModelChoiceField(queryset=Pais.objects.all(), empty_label="Pais", required = False, widget=forms.Select(attrs={'class': 'full', }))
    ciudad_hidden = forms.CharField(widget=forms.HiddenInput())
    genero = forms.ChoiceField(choices=genero, required = False, widget=forms.RadioSelect())

class ResumenForm(forms.Form):
    resumen = forms.CharField(required=True, widget=forms.Textarea)

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


class IdiomaForm(forms.Form):

    idioma = forms.ModelMultipleChoiceField(queryset= Idioma.objects.all(), required = False, widget=forms.SelectMultiple(attrs={'class': 'full'}))

class ConocimientoForm(forms.Form):

    # conocimiento = forms.ModelMultipleChoiceField(queryset=Conocimiento.objects.all(),  required = False, widget=forms.SelectMultiple(attrs={'class': 'full', }))
    conocimientos_hidden        = forms.CharField(widget=forms.HiddenInput(), required = False)
    conocimientos_nuevos_hidden = forms.CharField(widget=forms.HiddenInput(), required = False)
    conocimientos_extras_hidden = forms.CharField(widget=forms.HiddenInput(), required = False)

class ExperienciaForm(forms.ModelForm):
    # fecha_desde = forms.DateField(widget=forms.DateInput())
    fecha_desde_hidden = forms.CharField(widget=forms.HiddenInput())
    fecha_hasta_hidden = forms.CharField(widget=forms.HiddenInput())
    # fecha_hasta = forms.DateField(required=False, widget=forms.DateInput())

    puestos = forms.CharField(required = True,  max_length = 50, widget=forms.TextInput(attrs={'placeholder': 'Puesto', 'class': 'full'}))
    puestos_hidden = forms.CharField(widget=forms.HiddenInput())

    empresas = forms.CharField(required = True,  max_length = 50, widget=forms.TextInput(attrs={'placeholder': 'Empresa', 'class': 'full'}))
    empresas_hidden = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = ExperienciaProfesional
        fields = ('descripcion',)
        widget = {
            'descripcion': forms.widgets.Textarea
        }


class VoluntariadoForm(forms.ModelForm):
    # fecha_desde = forms.DateField(widget=forms.DateInput())
    fecha_desde_hidden = forms.CharField(widget=forms.HiddenInput())
    fecha_hasta_hidden = forms.CharField(widget=forms.HiddenInput())
    # fecha_hasta = forms.DateField(required=False, widget=forms.DateInput())
    cargo = forms.CharField(required = True,  max_length = 50, widget=forms.TextInput(attrs={'placeholder': 'Función', 'class': 'full'}))
    organizacion = forms.CharField(required = True,  max_length = 50, widget=forms.TextInput(attrs={'placeholder': 'Organización/Evento', 'class': 'full'}))
    class Meta:
        model = Voluntariado
        fields = ('cargo', 'organizacion', 'descripcion')

class ActividadesExtraForm(forms.ModelForm):
    class Meta:
        model = ActividadesExtra
        fields = ('organizacion', 'descripcion')

class EvaluacionForm(forms.ModelForm):
    class Meta:
        model = EvaluacionEmpresa
        fields = ('linea_carrera', 'flexibilidad_horarios', 'ambiente_trabajo', 'salarios')
        



