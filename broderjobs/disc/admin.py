from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Pregunta)

admin.site.register(models.Respuesta)

admin.site.register(models.Perfil)

class PatronPerfil(admin.ModelAdmin):
    list_display = ('Perfil', 'nro_patron', 'orden')
admin.site.register(models.PatronPerfil)
