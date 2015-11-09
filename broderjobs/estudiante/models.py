
from django.db import models
from main.models import Persona, Pais, Ciudad, GradoEstudio, Universidad, Carrera, TipoPuesto, CargaHoraria


class Estudiante(models.Model):
    persona = models.OneToOneField(Persona)
    grado_estudio = models.ForeignKey(GradoEstudio,default=None, null=True, blank=True )
    universidad = models.ForeignKey(Universidad,default=None, null=True, blank=True )
    carrera = models.ForeignKey(Carrera, default=None, null=True, blank=True )
    semestre_inicio_estudio = models.IntegerField(default=0, blank=True)
    ano_inicio_estudio = models.IntegerField(default=0, blank=True)
    semestre_graduacion = models.IntegerField(default=0, blank=True)
    ano_graduacion= models.IntegerField(default=0, blank= True)
    pais = models.ForeignKey(Pais, default=None, null=True, blank=True )
    ciudad = models.ForeignKey(Ciudad, default=None, null=True, blank=True )
    #carga_horaria = models.ForeignKey(CargaHoraria, null=True)

    def __unicode__(self):
		return '%s' % (self.persona)