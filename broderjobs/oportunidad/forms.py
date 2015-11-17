# coding=utf-8
from django import forms
from django.forms import ModelForm, Textarea, RadioSelect, TextInput, DateInput, SelectMultiple
from models import Oportunidad, TipoPuesto, CargaHoraria, Universidad, Idioma, Conocimiento, Beneficio, GradoEstudio, TipoRemuneracion, Carrera

class OportunidadForm(forms.ModelForm):

    class Meta:
        model = Oportunidad
        fields = ('titulo', 'carga_horaria', 'pais', 'ciudad', 'remuneracion', 'remuneracion_min', 'remuneracion_max',
                  'fecha_cese', 'beneficio', 'resumen', 'carga_horaria', 'tipo_puesto', 'remuneracion')
        widgets = {
            'titulo': TextInput(attrs={'placeholder': 'escriba el titulo de su vacacnte', 'class': 'full'}),
            'carga_horaria': RadioSelect(),
            'tipo_puesto': RadioSelect(),
            'remuneracion': RadioSelect(),
            'resumen': Textarea(),
            'remuneracion_min': TextInput(attrs={'placeholder': 'Valor minimo'}),
            'remuneracion_max': TextInput(attrs={'placeholder': 'Valor maximo'}),
            'fecha_cese': DateInput(attrs={'placeholder': 'Dia / Mes / Año'}),
            'beneficio': SelectMultiple()
        }
    def __init__(self, *args, **kwargs):
        super(OportunidadForm, self).__init__(*args, **kwargs)
        self.fields['carga_horaria'].empty_label = None
        self.fields['tipo_puesto'].empty_label = None
        self.fields['remuneracion'].empty_label = None
        self.fields['beneficio'].empty_label = None
        self.fields['pais'].empty_label = "Pais"
        self.fields['ciudad'].empty_label = "Ciudad"

class OportunidadCrearForm(OportunidadForm):

    grado_estudio = forms.ModelChoiceField(queryset=GradoEstudio.objects.all(), empty_label="Grado Estudio", required = False, widget=forms.Select(attrs={'class': 'full', }))
    universidad = forms.ModelMultipleChoiceField(queryset=Universidad.objects.all(), required = False, widget=forms.SelectMultiple(attrs={'class': 'full', }))
    idioma = forms.ModelMultipleChoiceField(queryset= Idioma.objects.all(), required = False, widget=forms.SelectMultiple(attrs={'class': 'full', }))
    conocimiento = forms.ModelMultipleChoiceField(queryset=Conocimiento.objects.all(),  required = False, widget=forms.SelectMultiple(attrs={'class': 'full', }))
    carrera = forms.ModelMultipleChoiceField(queryset=Carrera.objects.all(),  required = False, widget=forms.SelectMultiple(attrs={'class': 'full', }))
