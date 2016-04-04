from django.contrib import admin
from . import models
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from broderjobs.settings import DEFAULT_FROM_EMAIL
from django import forms



class CarreraInline(admin.TabularInline):
    model = models.Carrera

# class RamasAdmin(admin.ModelAdmin):
#     inlines = [CarreraInline]
#
#     def add_view(self, request, form_url = '', extra_context = None):
#         self.readonly_fields = ()
#         return super(RamasAdmin, self).add_view(request, form_url, extra_context)


class RamaCarreraForm(forms.ModelForm):
    class Meta:
        model = models.RamaCarrera
        fields = ('descripcion', 'fecha_creacion')

    carreras = forms.ModelMultipleChoiceField(queryset=models.Carrera.objects.all(), widget=forms.CheckboxSelectMultiple(),)

    def __init__(self, *args, **kwargs):
        super(RamaCarreraForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['carreras'].initial = self.instance.carrera_set.all()

    def save(self, *args, **kwargs):
        # FIXME: 'commit' argument is not handled
        # TODO: Wrap reassignments into transaction
        # NOTE: Previously assigned RamaCarreras are silently reset
        instance = super(RamaCarreraForm, self).save(commit=False)
        self.fields['carreras'].initial.update(rama_carrera=None)
        self.cleaned_data['carreras'].update(rama_carrera=instance)
        return instance


class RamasAdmin(admin.ModelAdmin):
    form = RamaCarreraForm

class PersonaAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        enviar = obj.enviar_correo
        obj.enviar_correo = False
        obj.save()

        if enviar == True and obj.estado == 'A':
            plaintext = get_template('correos/CuentaActivaSubject.txt')
            htmly     = get_template('correos/CuentaActiva.html')
            d = Context({ 'nombre': obj.usuario.first_name, 'email': obj.usuario.email,
                          'domain': request.META['HTTP_HOST'],
                          'site_name': 'your site',
                          'uid': urlsafe_base64_encode(force_bytes(obj.usuario.pk)),
                          'user': obj.usuario,
                          'token': default_token_generator.make_token(obj.usuario),
                          'protocol': 'http'
                        })
            subject, from_email, to = 'Su Cuenta ha sido Activada en BroderJobs.com', DEFAULT_FROM_EMAIL, obj.usuario.email
            text_content = plaintext.render(d)
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

admin.site.register(models.Persona, PersonaAdmin)

admin.site.register(models.GradoEstudio)

admin.site.register(models.Pais)

admin.site.register(models.Ciudad)

admin.site.register(models.Universidad)

admin.site.register(models.Carrera)

admin.site.register(models.TipoCarrera)

admin.site.register(models.RamaCarrera, RamasAdmin)

admin.site.register(models.IdiomaBase)

admin.site.register(models.Idioma)

admin.site.register(models.CargaHoraria)

admin.site.register(models.TipoPuesto)

admin.site.register(models.Conocimiento)

admin.site.register(models.TipoRemuneracion)

admin.site.register(models.Beneficio)

admin.site.register(models.PeriodosGraduacion)





