from django.contrib import admin
from .models import Estudiante, Resumen, ActividadesExtra, ExperienciaProfesional, Voluntariado, EstudianteIdioma

# Register your models here.
admin.site.register(Estudiante)

admin.site.register(Resumen)

admin.site.register(ActividadesExtra)

admin.site.register(ExperienciaProfesional)

admin.site.register(EstudianteIdioma)

admin.site.register(Voluntariado)


