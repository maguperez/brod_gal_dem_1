from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Persona(models.Model):
    usuario = models.OneToOneField(User)
    telefono = models.CharField(default=None, null=True, blank=True, max_length=20)
    fecha_nacimiento = models.DateField(null=True)
    tipo_persona = models.CharField(max_length=1,default="E")

    def __unicode__(self):
		return '%s' % (self.usuario.first_name+ " "+self.usuario.last_name)

class GradoEstudio(models.Model):
    descripcion = models.CharField(max_length="50")

    def __unicode__(self):
		return '%s' % (self.descripcion)

class Pais(models.Model):
    descripcion = models.CharField(max_length="50")

    def __unicode__(self):
		return self.descripcion

class Ciudad(models.Model):
    pais = models.ForeignKey(Pais)
    descripcion = models.CharField(max_length="50")

    def __unicode__(self):
		return self.descripcion

class Universidad(models.Model):
    descripcion = models.CharField(max_length="50")

    def __unicode__(self):
		return self.descripcion

class Carrera(models.Model):
    descripcion = models.CharField(max_length="50")

    def __unicode__(self):
		return self.descripcion

class TipoPuesto:
    descripcion = models.CharField(max_length="50")

    def __unicode__(self):
		return self.descripcion

class CargaHoraria:
    descripcion = models.CharField(max_length="50")

    def __unicode__(self):
		return self.descripcion

