# coding=utf-8
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from models import Empresa, Representante, Sector

class InfoGeneralForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ('nombre', 'RUC', 'quienes_somos', 'sector', 'numero_funcionarios', 'facturacion_anual', 'ano_fundacion', 'pais', 'ciudad', 'website')
        widget = {
            'quienessomos': forms.widgets.Textarea(),
        }

    @property
    def helper(self):
        helper = FormHelper()
        helper.form_tag = False # don't render form DOM element
        helper.render_unmentioned_fields = True # render all fields
        return helper

class LogoForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ('logo', 'nombre')

    @property
    def helper(self):
        helper = FormHelper()
        helper.form_tag = False # don't render form DOM element
        helper.render_unmentioned_fields = True # render all fields
        return helper