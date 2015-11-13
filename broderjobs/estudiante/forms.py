# coding=utf-8
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from django.forms.models import ModelChoiceField
from models import GradoEstudio, Universidad, Carrera, Pais, Ciudad, Estudiante, TipoPuesto, CargaHoraria
import datetime
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

    @property
    def helper(self):
        helper = FormHelper()
        helper.form_tag = False # don't render form DOM element
        helper.render_unmentioned_fields = True # render all fields
        helper.label_class = 'col-md-2'
        helper.field_class = 'col-md-10'
        return helper


