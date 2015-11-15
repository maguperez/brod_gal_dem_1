# coding=utf-8
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from django.forms.models import ModelChoiceField
from models import GradoEstudio, Universidad, Carrera, Pais, Ciudad, Estudiante, TipoPuesto, CargaHoraria
import datetime
from django.contrib.auth.models import User
from main import utilitarios

class RegistroCVForm(forms.ModelForm):
    class Meta:
            model = Estudiante
            fields = ('grado_estudio', 'carrera', 'universidad', 'semestre_inicio_estudio', 'ano_inicio_estudio', 'semestre_graduacion',
                     'ano_graduacion', 'pais', 'ciudad', 'tipo_puesto', 'carga_horaria')

    def __init__(self, *args, **kwargs):
        super(RegistroCVForm, self).__init__(*args, **kwargs)

        #Carga items a Grado de Estudio
        grado_estudios = []
        for grado_estudio in GradoEstudio.objects.all():
            grado_estudios.append((grado_estudio.id, grado_estudio.descripcion))
        self.fields['grado_estudio'].widget = forms.Select(attrs={'class': 'full'})
        self.fields['grado_estudio'].choices = grado_estudios

        #Carga items a Carrera
        carreras = []
        for carrera in Carrera.objects.all():
            carreras.append((carrera.id, carrera.descripcion))
        self.fields['carrera'].widget =forms.Select(attrs={'class': 'full'})
        self.fields['carrera'].choices = carreras


        #Carga items a Universidad
        universidades = []
        for universidad in Universidad.objects.all():
            universidades.append((universidad.id, universidad.descripcion))
        self.fields['universidad'].widget =forms.Select(attrs={'class': 'full'})
        self.fields['universidad'].choices = universidades

        #Carga items Semestre
        items_semestre = utilitarios.semestre_rango()
        self.fields['semestre_inicio_estudio'].widget = forms.Select(attrs={'class': 'half-2'})
        self.fields['semestre_graduacion'].widget = forms.Select(attrs={'class': 'half-2'})

        self.fields['semestre_inicio_estudio'].choices = items_semestre
        self.fields['semestre_graduacion'].choices = items_semestre

        #Carga items a años

        items_anos = utilitarios.anos_rango()
        self.fields['ano_inicio_estudio'].widget = forms.Select(attrs={'class': 'half-1'})
        self.fields['ano_inicio_estudio'].choices = items_anos

        self.fields['ano_graduacion'].widget = forms.Select(attrs={'class': 'half-1'})
        self.fields['ano_graduacion'].choices = items_anos

        #Carga items a Psis
        paises = []
        for pais in Pais.objects.all():
            paises.append((pais.id, pais.descripcion))
        self.fields['pais'].widget =forms.Select(attrs={'class': 'full'})
        self.fields['pais'].choices = paises

        #Carga items a ciudad
        ciudades = []
        for ciudad in Ciudad.objects.all():
            ciudades.append((ciudad.id, ciudad.descripcion))
        self.fields['ciudad'].widget =forms.Select(attrs={'class': 'full'})
        self.fields['ciudad'].choices = ciudades

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

# END CLASS #

class ResumenForm(forms.Form):
    resumen = forms.CharField(required=True, widget=forms.Textarea)

# END CLASS

class FotoForm(forms.Form):
    foto = forms.FileField(label='Selecione Imagen de Perfil')


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

class InfoPersonalForm(forms.Form):
    grado_estudios = []
    for grado_estudio in GradoEstudio.objects.all():
        grado_estudios.append((grado_estudio.id, grado_estudio.descripcion))

    carreras = []
    for carrera in Carrera.objects.all():
        carreras.append((carrera.id, carrera.descripcion))

    universidades = []
    for universidad in Universidad.objects.all():
        universidades.append((universidad.id, universidad.descripcion))

    paises = []
    for pais in Pais.objects.all():
        paises.append((pais.id, pais.descripcion))

    ciudades = []
    for ciudad in Ciudad.objects.all():
        ciudades.append((ciudad.id, ciudad.descripcion))

    items_anos = utilitarios.anos_rango()
    #grado_estudio = forms.ChoiceField(choices= grado_estudios, required = False )
    #carrera = forms.ChoiceField(choices= carreras, required = False, widget=forms.Select(attrs={'class': 'full'}))
    #universidad = forms.ChoiceField(choices= universidades, required = False, widget=forms.Select(attrs={'class': 'full'}))
    #semestre_inicio_estudio = forms.ChoiceField(choices=utilitarios.semestre_rango(), required = False, widget=forms.Select(attrs={'class': 'half-2'}))
    #ano_inicio_estudio = forms.ChoiceField(choices=utilitarios.anos_rango(), required = False, widget=forms.Select(attrs={'class': 'half-1'}))
    semestre_graduacion = forms.ChoiceField(choices=utilitarios.semestre_rango(), required = False, widget=forms.Select(attrs={'class': 'half-2'}))
    ano_graduacion = forms.ChoiceField(choices=utilitarios.anos_rango(), required = False, widget=forms.Select(attrs={'class': 'half-1'}))
    pais = forms.ChoiceField(choices= paises, required = False, widget=forms.Select(attrs={'class': 'full'}))
    ciudad = forms.ChoiceField(choices= ciudades, required = False, widget=forms.Select(attrs={'class': 'full'}))
    email = UniqueUserEmailField(required = True, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    fecha_nacimiento = forms.DateField(required=False)
    ano = forms.ChoiceField(choices=utilitarios.anos_nacimiento(), required = False, widget=forms.Select(attrs={'class': 'cumpleanos', }))
    mes = forms.ChoiceField(choices=utilitarios.meses_del_ano(), required = False, widget=forms.Select(attrs={'class': 'cumpleanos'}))
    dia = forms.ChoiceField(choices=utilitarios.anos_nacimiento(), required = False, widget=forms.Select(attrs={'class': 'cumpleanos'}))
    telefono = forms.CharField(required = False, max_length = 20, widget=forms.TextInput(attrs={'placeholder': 'Celular'}))

