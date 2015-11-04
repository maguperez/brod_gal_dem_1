from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EstudianteRegistro(forms.Form):
    grado_estudio = form.w
    universidad = models.OneToOneField(Universidad, default=0)
    carerra = models.OneToOneField(Carrera, default=0)
    pais = models.OneToOneField(Pais, default=0)
    ciudad = models.OneToOneField(Ciudad, default=0)
    #tipo_puesto = models.OneToOneRel(Estudiante_TipoPuesto, default=0),
    carga_horaria = models.CharField(max_length=1, null=True)


