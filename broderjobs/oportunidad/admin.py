from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Oportunidad)

class PostulacionAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'oportunidad')

admin.site.register(models.Postulacion, PostulacionAdmin)

admin.site.register(models.ProcesoFase)