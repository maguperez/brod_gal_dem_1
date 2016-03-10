from django.contrib import admin
from . import models

# Register your models here.

class OportunidadAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'empresa', 'estado_oportunidad')

admin.site.register(models.Oportunidad, OportunidadAdmin)


class OportunidadCompatibilidadAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'oportunidad', 'compatibilidad_promedio', 'compatibilidad_cultural', 'compatibilidad_academica')
admin.site.register(models.OportunidadCompatibilidad, OportunidadCompatibilidadAdmin)

class PostulacionAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'oportunidad')

admin.site.register(models.Postulacion, PostulacionAdmin)

admin.site.register(models.ProcesoFase)

admin.site.register(models.BeneficioExtra)