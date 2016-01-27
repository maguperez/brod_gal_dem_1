# coding=utf-8
from django import forms
from django.forms import ModelForm, Textarea, RadioSelect, TextInput, DateInput, SelectMultiple, Select
from models import Oportunidad, TipoPuesto, CargaHoraria, Universidad, Idioma, Conocimiento, Beneficio, GradoEstudio, \
    TipoRemuneracion, Carrera, Pais


class OportunidadForm(forms.ModelForm):

    # paises = forms.CharField(required = True,  max_length = 50, widget=forms.TextInput(attrs={'placeholder': 'País', 'class': 'full'}))
    # paises_hidden = forms.CharField(widget=forms.HiddenInput())
    #
    # ciudades = forms.CharField(required = True,  max_length = 50, widget=forms.TextInput(attrs={'placeholder': 'Ciudad', 'class': 'full'}))
    ciudad_hidden = forms.CharField(widget=forms.HiddenInput(), required = False)
    periodo_graduacion_hidden = forms.CharField(widget=forms.HiddenInput(), required = False)
    pais = forms.ModelChoiceField(queryset=Pais.objects.all(), empty_label="Pais", required = False, widget=forms.Select(attrs={'class': 'full', }))
    # ciudad = forms.ChoiceField(required = False, widget=forms.Select(attrs={'class': 'full'}))
    beneficios_hidden = forms.CharField(widget=forms.HiddenInput(), required = False)
    beneficios_nuevos_hidden = forms.CharField(widget=forms.HiddenInput(), required = False)
    beneficios_extras_hidden = forms.CharField(widget=forms.HiddenInput(), required = False)

    class Meta:
        model = Oportunidad
        fields = ('titulo', 'carga_horaria', 'remuneracion', 'remuneracion_min', 'remuneracion_max',
                  # 'fecha_cese', 'beneficio', 'resumen', 'carga_horaria', 'tipo_puesto', 'estado', 'estado_oportunidad',
                  'fecha_cese', 'resumen', 'carga_horaria', 'tipo_puesto', 'estado', 'estado_oportunidad',
                  'grado_estudio', 'universidad', 'idioma', 'conocimiento', 'carrera', 'direccion_map', 'longitud', 'latitud',
                  'tipo_carrera')
        widgets = {
            'titulo': TextInput(attrs={'placeholder': 'Escriba el titulo de su vacante', 'class': 'full'}),
            'carga_horaria': RadioSelect(),
            'tipo_puesto': RadioSelect(),
            'remuneracion': RadioSelect(),
            'resumen': Textarea(),
            'remuneracion_min': TextInput(attrs={'placeholder': 'Valor minimo'}),
            'remuneracion_max': TextInput(attrs={'placeholder': 'Valor maximo'}),
            'fecha_cese': DateInput(attrs={'placeholder': 'Dia / Mes / Año'}),
            'direccion_map': TextInput(attrs={'placeholder': 'Direccion', 'class': 'full'}),
            'longitud': TextInput(attrs={'placeholder': 'longitud'}),
            'latitud': TextInput(attrs={'placeholder': 'latitud'}),
            'carrera': SelectMultiple(attrs={'class': 'full'}),
            'idioma': SelectMultiple(attrs={'class': 'full'}),
            'grado_estudio': Select(attrs={'class': 'full'}),
            'conocimiento': SelectMultiple(attrs={'class': 'full'}),
            'estado_oportunidad': Select(attrs={'disabled':'disabled'})
        }

    def __init__(self, *args, **kwargs):
        super(OportunidadForm, self).__init__(*args, **kwargs)
        self.fields['carga_horaria'].empty_label = None
        self.fields['tipo_puesto'].empty_label = None
        self.fields['remuneracion'].empty_label = None

        self.fields['grado_estudio'].empty_label = "Seleccione"
        self.fields['pais'].empty_label = "Pais"

class OportunidadCrearForm(OportunidadForm):

    grado_estudio = forms.ModelChoiceField(queryset=GradoEstudio.objects.all(), empty_label="Grado Estudio", required = False, widget=forms.Select(attrs={'class': 'full', }))
    universidad = forms.ModelMultipleChoiceField(queryset=Universidad.objects.all(), required = False, widget=forms.SelectMultiple(attrs={'class': 'full', }))
    idioma = forms.ModelMultipleChoiceField(queryset= Idioma.objects.all(), required = False, widget=forms.SelectMultiple(attrs={'class': 'full', }))
    conocimiento = forms.ModelMultipleChoiceField(queryset=Conocimiento.objects.all(),  required = False, widget=forms.SelectMultiple(attrs={'class': 'full', }))
    carrera = forms.ModelMultipleChoiceField(queryset=Carrera.objects.all(),  required = False, widget=forms.SelectMultiple(attrs={'class': 'full', }))

# class OportunidadEditarForm(forms.Form):
#
#     titulo = forms.TextInput(attrs={'placeholder': 'escriba el titulo de su vacacnte', 'class': 'full'}),
#     carga_horaria = forms.ModelChoiceField(queryset=CargaHoraria.objects.all(), widget= forms.RadioSelect() ),
#     tipo_puesto = forms.ModelChoiceField(queryset=TipoPuesto.objects.all(), widget= forms.RadioSelect() ),
#     remuneracion = forms.ModelChoiceField(queryset=TipoRemuneracion.objects.all(), widget= forms.RadioSelect()),
#     resumen = forms.Textarea(),
#     remuneracion_min =  forms.TextInput(attrs={'placeholder': 'Valor minimo'}),
#     remuneracion_max = forms.TextInput(attrs={'placeholder': 'Valor maximo'}),
#     fecha_cese = forms.DateInput(attrs={'placeholder': 'Dia / Mes / Año'}),
#     beneficio = forms.ModelChoiceField(queryset=Beneficio.objects.all(), widget= forms.RadioSelect()),
#
#     grado_estudio = forms.ModelChoiceField(queryset=GradoEstudio.objects.all(), empty_label="Grado Estudio", required = False, widget=forms.Select(attrs={'class': 'full', }))
#     universidad = forms.ModelMultipleChoiceField(queryset=Universidad.objects.all(), required = False, widget=forms.SelectMultiple(attrs={'class': 'full', }))
#     idioma = forms.ModelMultipleChoiceField(queryset= Idioma.objects.all(), required = False, widget=forms.SelectMultiple(attrs={'class': 'full', }))
#     conocimiento = forms.ModelMultipleChoiceField(queryset=Conocimiento.objects.all(),  required = False, widget=forms.SelectMultiple(attrs={'class': 'full', }))
#     carrera = forms.ModelMultipleChoiceField(queryset=Carrera.objects.all(),  required = False, widget=forms.SelectMultiple(attrs={'class': 'full', }))
#
#     def __init__(self, *args, **kwargs):
#         super(OportunidadEditarForm, self).__init__(*args, **kwargs)

