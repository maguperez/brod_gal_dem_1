# coding=utf-8
from django import forms
from django.forms import ModelForm, Textarea, RadioSelect, TextInput, DateInput, SelectMultiple, Select
from models import Oportunidad, TipoPuesto, CargaHoraria, Universidad, Idioma, Conocimiento, Beneficio, GradoEstudio, \
    TipoRemuneracion, Carrera, Pais
from main.utils import genero


class OportunidadForm(forms.ModelForm):

    ciudad_hidden = forms.CharField(widget=forms.HiddenInput(), required = False)
    periodo_graduacion_hidden = forms.CharField(widget=forms.HiddenInput(), required = False)
    pais = forms.ModelChoiceField(queryset=Pais.objects.all(), empty_label="Pais", required = False, widget=forms.Select(attrs={'class': 'full actualizar', }))
    beneficios_hidden = forms.CharField(widget=forms.HiddenInput(), required = False)
    beneficios_nuevos_hidden = forms.CharField(widget=forms.HiddenInput(), required = False)
    beneficios_extras_hidden = forms.CharField(widget=forms.HiddenInput(), required = False)

    class Meta:
        model = Oportunidad
        fields = ('titulo', 'carga_horaria', 'remuneracion', 'remuneracion_min', 'remuneracion_max',
                  # 'fecha_cese', 'beneficio', 'resumen', 'carga_horaria', 'tipo_puesto', 'estado', 'estado_oportunidad',
                  'fecha_cese', 'resumen','edad_desde', 'edad_hasta', 'genero', 'carga_horaria', 'tipo_puesto', 'estado', 'estado_oportunidad',
                  'grado_estudio', 'universidad', 'idioma', 'conocimiento', 'carrera', 'direccion_map', 'longitud', 'latitud',
                  'tipo_carrera')
        widgets = {
            'titulo': TextInput(attrs={'placeholder': 'Escriba el título de su vacante', 'class': 'full'}),
            'carga_horaria': RadioSelect(attrs={'class': 'actualizar'}),
            'tipo_puesto': RadioSelect(attrs={'class': 'actualizar'}),
            'remuneracion': RadioSelect(attrs={'class': 'actualizar'}),
            'resumen': Textarea(),
            'remuneracion_min': TextInput(attrs={'placeholder': 'Valor mínimo'}),
            'remuneracion_max': TextInput(attrs={'placeholder': 'Valor máximo'}),
            'fecha_cese': DateInput(attrs={'placeholder': 'Día / Mes / Año'}),
            'direccion_map': TextInput(attrs={'placeholder': 'Dirección', 'class': 'full'}),
            'longitud': TextInput(attrs={'placeholder': 'longitud'}),
            'latitud': TextInput(attrs={'placeholder': 'latitud'}),
            'carrera': SelectMultiple(attrs={'class': 'full actualizar'}),
            'universidad': SelectMultiple(attrs={'class': 'actualizar'}),
            'idioma': SelectMultiple(attrs={'class': 'full actualizar'}),
            'grado_estudio': Select(attrs={'class': 'full actualizar'}),
            'conocimiento': SelectMultiple(attrs={'class': 'full actualizar'}),
            'estado_oportunidad': Select(attrs={'disabled':'disabled'}),
            'edad_desde': TextInput(attrs={'class': 'actualizar', 'placeholder': 'Desde', 'type': 'number'}),
            'edad_hasta': TextInput(attrs={'class': 'actualizar', 'placeholder': 'Hasta', 'type': 'number'}),
            'genero': Select(attrs={'class': 'actualizar'}),
        }

    def __init__(self, *args, **kwargs):
        super(OportunidadForm, self).__init__(*args, **kwargs)
        self.fields['carga_horaria'].empty_label = None
        self.fields['tipo_puesto'].empty_label = None
        self.fields['remuneracion'].empty_label = None

        self.fields['grado_estudio'].empty_label = "Seleccione"
        self.fields['pais'].empty_label = "País"
        self.fields['genero'].empty_label = "Indistinto"
        # self.fields['genero'].choices = genero()


class OportunidadCrearForm(OportunidadForm):

    grado_estudio = forms.ModelChoiceField(queryset=GradoEstudio.objects.all(), empty_label="Grado Estudio", required = False, widget=forms.Select(attrs={'class': 'full', }))
    universidad = forms.ModelMultipleChoiceField(queryset=Universidad.objects.all(), required = False, widget=forms.SelectMultiple(attrs={'class': 'full actualizar', }))
    idioma = forms.ModelMultipleChoiceField(queryset= Idioma.objects.all(), required = False, widget=forms.SelectMultiple(attrs={'class': 'full actualizar', }))
    conocimiento = forms.ModelMultipleChoiceField(queryset=Conocimiento.objects.all(),  required = False, widget=forms.SelectMultiple(attrs={'class': 'full actualizar', }))
    carrera = forms.ModelMultipleChoiceField(queryset=Carrera.objects.all(),  required = False, widget=forms.SelectMultiple(attrs={'class': 'full actualizar', }))

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

