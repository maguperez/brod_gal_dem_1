from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Pregunta)

admin.site.register(models.Respuesta)

class RepuestaEstudianteAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'respuesta', 'letra_mas', 'letra_menos')
admin.site.register(models.RespuestaEstudiante, RepuestaEstudianteAdmin)
