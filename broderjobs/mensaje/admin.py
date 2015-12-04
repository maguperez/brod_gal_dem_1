from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Mensaje)

admin.site.register(models.Mensaje_Destinatario)

