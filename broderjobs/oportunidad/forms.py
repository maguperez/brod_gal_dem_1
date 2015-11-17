# coding=utf-8
from django import forms
from models import Oportunidad, TipoPuesto, CargaHoraria, Universidad, Idioma, Conocimiento, Beneficio, GradoEstudio, TipoRemuneracion

class OportunidadForm(forms.ModelForm):

    class Meta:
        model = Oportunidad
        fields = ('titulo', 'carga_horaria', 'pais', 'ciudad', 'remuneracion', 'remuneracion_min', 'remuneracion_max',
                  'fecha_cese', 'tipo_puesto', 'beneficio', 'resumen' )


class OportunidadCrearForm(OportunidadForm):

    grado_estudio = forms.ChoiceField(required = False, widget=forms.SelectMultiple(attrs={'class': 'full', }))
    universidad = forms.ChoiceField(required = False, widget=forms.SelectMultiple(attrs={'class': 'full', }))
    idioma = forms.ChoiceField(required = False, widget=forms.SelectMultiple(attrs={'class': 'full', }))
    conocimiento = forms.ChoiceField(required = False, widget=forms.SelectMultiple(attrs={'class': 'full', }))
    beneficio = forms.ChoiceField(required = False, widget=forms.SelectMultiple(attrs={'class': 'full', }))

    def __init__(self, *args, **kwargs):
        super(OportunidadCrearForm, self).__init__(*args, **kwargs)

        #Carga Tipo de
        self.fields["tipo_puesto"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["tipo_puesto"].help_text = ""
        self.fields["tipo_puesto"].queryset = TipoPuesto.objects.all()

        #Carga Horaria
        self.fields["carga_horaria"].widget = forms.widgets.RadioSelect()
        self.fields["carga_horaria"].queryset = CargaHoraria.objects.all()

        #TipoRemuneracion
        self.fields["remuneracion"].widget = forms.widgets.RadioSelect()
        self.fields["remuneracion"].queryset = TipoRemuneracion.objects.all()

        #TipoRemuneracion
        self.fields["grado_estudio"].widget = forms.widgets.SelectMultiple()
        self.fields["grado_estudio"].queryset = GradoEstudio.objects.all()

        #TipoRemuneracion
        self.fields["universidad"].widget = forms.widgets.SelectMultiple()
        self.fields["universidad"].queryset = Universidad.objects.all()

        #TipoRemuneracion
        self.fields["idioma"].widget = forms.widgets.SelectMultiple()
        self.fields["idioma"].queryset = Idioma.objects.all()

        # #TipoRemuneracion
        # self.fields["conocimiento"].queryset = Conocimiento.objects.all()

        self.fields["conocimiento"].widget = forms.widgets.SelectMultiple()

        #TipoRemuneracion
        self.fields["beneficio"].widget = forms.widgets.SelectMultiple()
        self.fields["beneficio"].queryset = Beneficio.objects.all()
