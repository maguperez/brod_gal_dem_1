# coding=utf-8
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from models import Empresa, Representante, Sector, EvaluacionEmpresa, Pais

class InfoGeneralForm(forms.ModelForm):

    ciudad_hidden = forms.CharField(widget=forms.HiddenInput(),required=False)
    pais = forms.ModelChoiceField(queryset=Pais.objects.all(), empty_label="Pais", required = False, widget=forms.Select(attrs={'class': 'full', }))

    class Meta:
        model = Empresa
        fields = ('nombre', 'RUC', 'quienes_somos', 'sector', 'numero_funcionarios', 'facturacion_anual', 'ano_fundacion',
                  'website','telefono')
        widget = {
            'quienessomos': forms.widgets.Textarea(),
        }


class LogoForm(forms.Form):
     logo = forms.ImageField(required=False, error_messages = {'invalid':'Porfavor seleccione una Imagen valida'}, widget=forms.FileInput)

class UbicacionForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ('longitud', 'latitud', 'direccion_map')

