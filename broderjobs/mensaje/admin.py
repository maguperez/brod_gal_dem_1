from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Mensaje)

admin.site.register(models.Mensaje_Destinatario)

class NotificacionAdmin(admin.ModelAdmin):
    list_display = ('usuario_destinatario', 'oportunidad', 'asunto', 'leido')
admin.site.register(models.Notificacion, NotificacionAdmin)

