from django.contrib import admin
from .models import Estudiante, Resumen, ActividadesExtra, ExperienciaProfesional, Voluntariado, ConocimientoExtra

# Register your models here.
admin.site.register(Estudiante)

admin.site.register(Resumen)

admin.site.register(ActividadesExtra)

admin.site.register(ConocimientoExtra)

admin.site.register(ExperienciaProfesional)

admin.site.register(Voluntariado)


