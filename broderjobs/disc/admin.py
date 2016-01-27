from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Pregunta)

admin.site.register(models.Respuesta)

admin.site.register(models.Perfil)

admin.site.register(models.DiscCodificacion)

class PatronPerfilAdmin(admin.ModelAdmin):
    list_display = ('perfil', 'nro_patron', 'orden')
admin.site.register(models.PatronPerfil, PatronPerfilAdmin)

class EstudianteRespuestasAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'pregunta', 'letra_mas', 'letra_menos')
admin.site.register(models.EstudianteRespuestas, EstudianteRespuestasAdmin)

class EstudiantePatronAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'patron_perfil')
admin.site.register(models.EstudiantePatron, EstudiantePatronAdmin)