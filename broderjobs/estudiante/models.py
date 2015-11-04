
from django.db import models
from main.models import Persona, Pais, Ciudad, GradoEstudio, Universidad, Carrera, TipoPuesto


class Estudiante(models.Model):
    persona = models.OneToOneField(Persona)
    grado_estudio = models.OneToOneField(GradoEstudio, default=0)
    universidad = models.OneToOneField(Universidad, default=0)
    carerra = models.OneToOneField(Carrera, default=0)
    pais = models.OneToOneField(Pais, default=0)
    ciudad = models.OneToOneField(Ciudad, default=0)
    #tipo_puesto = models.OneToOneRel(Estudiante_TipoPuesto, default=0),
    carga_horaria = models.CharField(max_length=1, null=True)

    def __unicode__(self):
		return self.persona