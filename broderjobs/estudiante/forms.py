# coding=utf-8
from django import forms
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from django.forms.models import ModelChoiceField
from .models import ExperienciaProfesional, Voluntariado, ActividadesExtra
from models import Persona, GradoEstudio, Universidad, Carrera, Pais, Ciudad, Estudiante, TipoPuesto, CargaHoraria,Idioma, Conocimiento, Puesto
import datetime

from main import utilitarios

class RegistroCVForm(forms.ModelForm):

    universidades = forms.CharField(required = True,  max_length = 50, widget=forms.TextInput(attrs={'placeholder': 'Universidades', 'class': 'full'}))
    universidades_hidden = forms.CharField(widget=forms.HiddenInput())

    carreras = forms.CharField(required = True,  max_length = 50, widget=forms.TextInput(attrs={'placeholder': 'Carreras', 'class': 'full'}))
    carreras_hidden = forms.CharField(widget=forms.HiddenInput())

    paises = forms.CharField(required = True,  max_length = 50, widget=forms.TextInput(attrs={'placeholder': 'País', 'class': 'full'}))
    paises_hidden = forms.CharField(widget=forms.HiddenInput())

    ciudades = forms.CharField(required = True,  max_length = 50, widget=forms.TextInput(attrs={'placeholder': 'Ciudad', 'class': 'full'}))
    ciudades_hidden = forms.CharField(widget=forms.HiddenInput())

    class Meta:
            model = Estudiante
            fields = ('grado_estudio', 'semestre_inicio_estudio', 'ano_inicio_estudio', 'semestre_graduacion',
                     'ano_graduacion', 'tipo_puesto', 'carga_horaria')

    def __init__(self, *args, **kwargs):
        super(RegistroCVForm, self).__init__(*args, **kwargs)

        #Carga items a Grado de Estudio
        grado_estudios = []
        grado_estudios.append(('', 'Seleccione'))
        for grado_estudio in GradoEstudio.objects.all():
            grado_estudios.append((grado_estudio.id, grado_estudio.descripcion))
        self.fields['grado_estudio'].widget = forms.Select(attrs={'class': 'full'})
        self.fields['grado_estudio'].choices = grado_estudios

        #Carga items a Carrera
        # carreras = []
        # carreras.append(('', ''))
        # for carrera in Carrera.objects.all():
        #     carreras.append((carrera.id, carrera.descripcion))
        # self.fields['carrera'].widget =forms.Select(attrs={'class': 'full'})
        # self.fields['carrera'].choices = carreras


        # #Carga items a Universidad
        # universidades = []
        # universidades.append(('', ''))
        # for universidad in Universidad.objects.all():
        #     universidades.append((universidad.id, universidad.descripcion))
        # self.fields['universidad'].widget =forms.Select(attrs={'class': 'full'})
        # self.fields['universidad'].choices = universidades

        #Carga items Semestre
        items_semestre = utilitarios.semestre_rango()
        self.fields['semestre_inicio_estudio'].widget = forms.Select(attrs={'class': 'half-medio'})
        self.fields['semestre_graduacion'].widget = forms.Select(attrs={'class': 'half-medio'})

        self.fields['semestre_inicio_estudio'].choices = items_semestre
        self.fields['semestre_graduacion'].choices = items_semestre

        #Carga items a años

        items_anos = utilitarios.anos_rango()
        self.fields['ano_inicio_estudio'].widget = forms.Select(attrs={'class': 'half-medio'})
        self.fields['ano_inicio_estudio'].choices = items_anos

        self.fields['ano_graduacion'].widget = forms.Select(attrs={'class': 'half-medio'})
        self.fields['ano_graduacion'].choices = items_anos

        #Carga items a Psis
        # paises = []
        # paises.append(('', ''))
        # for pais in Pais.objects.all():
        #     paises.append((pais.id, pais.descripcion))
        # self.fields['pais'].widget =forms.Select(attrs={'class': 'full'})
        # self.fields['pais'].choices = paises

        #Carga items a ciudad
        # ciudades = []
        # ciudades.append(('', ''))
        # for ciudad in Ciudad.objects.all():
        #     ciudades.append((ciudad.id, ciudad.descripcion))
        # self.fields['ciudad'].widget =forms.Select(attrs={'class': 'full'})
        # self.fields['ciudad'].choices = ciudades

        #Carga Tipo de
        self.fields["tipo_puesto"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["tipo_puesto"].help_text = ""
        self.fields["tipo_puesto"].queryset = TipoPuesto.objects.all()

        #Carga Horaria
        cargas = []
        for carga in CargaHoraria.objects.all():
            cargas.append((carga.id, carga.descripcion))
        self.fields["carga_horaria"].widget = forms.widgets.RadioSelect()
        self.fields["carga_horaria"].choices =cargas

class FotoForm(forms.Form):

   foto = forms.ImageField(label= "Seleccione la Imagen que desea cargar")
   #  class Meta:
   #      model = Estudiante
   #      fields = ('foto', 'persona')

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



