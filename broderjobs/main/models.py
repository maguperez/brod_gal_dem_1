from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Persona(models.Model):
    usuario = models.OneToOneField(User)
    telefono = models.CharField(default=None, null=True, blank=True, max_length=20)
    fecha_nacimiento = models.DateField(null=True)
    tipo_persona = models.CharField(max_length=1, default="E")

    def __unicode__(self):
		return unicode(self.usuario.first_name+ " "+self.usuario.last_name) or u''

class GradoEstudio(models.Model):
    descripcion = models.CharField(max_length="50")

    def __unicode__(self):
		return unicode(self.descripcion) or u''

class Pais(models.Model):
    descripcion = models.CharField(max_length="50")

    def __unicode__(self):
		return unicode(self.descripcion) or u''

class Ciudad(models.Model):
    pais = models.ForeignKey(Pais)
    descripcion = models.CharField(max_length="50")

    def __unicode__(self):
		return unicode(self.descripcion) or u''

class Universidad(models.Model):
    descripcion = models.CharField(max_length="50")

    def __unicode__(self):
		return unicode(self.descripcion) or u''

class Carrera(models.Model):
    descripcion = models.CharField(max_length="50")

    def __unicode__(self):
		return unicode(self.descripcion) or u''

class TipoPuesto(models.Model):
    descripcion = models.CharField(max_length="50")

    def __unicode__(self):
		return unicode(self.descripcion) or u''

class CargaHoraria(models.Model):
    descripcion = models.CharField(max_length="50")

    def __unicode__(self):
		return unicode(self.descripcion) or u''

class Idioma(models.Model):
    descripcion = models.CharField(max_length="50")

    def __unicode__(self):
		return unicode(self.descripcion) or u''

class Conocimiento(models.Model):
    descripcion = models.CharField(max_length="50")

    def __unicode__(self):
		return unicode(self.descripcion) or u''

class TipoRemuneracion(models.Model):
    descripcion = models.CharField(max_length="50")

    def __unicode__(self):
		return unicode(self.descripcion) or u''

class Beneficio(models.Model):
    descripcion = models.CharField(max_length="50")

    def __unicode__(self):
		return unicode(self.descripcion) or u''




