from django.db import models
from django.contrib.auth.models import User

from main import utils
items_registro = utils.estado_registro()

class Persona(models.Model):
    usuario = models.OneToOneField(User)
    telefono = models.CharField(default=None, null=True, blank=True, max_length=20)
    fecha_nacimiento = models.DateField(null=True)
    tipo_persona = models.CharField(max_length=1, default="E")
    genero = models.CharField(choices=utils.genero(), max_length=1, default='', null=True, blank=True)

    fecha_creacion = models.DateField(default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=None, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    def __unicode__(self):
		return unicode(self.usuario.first_name+ " "+self.usuario.last_name) or u''

class GradoEstudio(models.Model):
    descripcion = models.CharField(max_length="50")

    orden = models.IntegerField(null= True, blank= True)
    fecha_creacion = models.DateField(default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=None, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    class Meta:
        ordering = ["orden"]

    def __unicode__(self):
		return unicode(self.descripcion) or u''

class Pais(models.Model):
    descripcion = models.CharField(max_length="50")

    orden = models.IntegerField(null= True, blank= True)
    fecha_creacion = models.DateField(default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=None, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    class Meta:
        ordering = ["orden"]

    def __unicode__(self):
		return unicode(self.descripcion) or u''

class Ciudad(models.Model):
    pais = models.ForeignKey(Pais)
    descripcion = models.CharField(max_length="50")

    orden = models.IntegerField(null= True, blank= True)
    fecha_creacion = models.DateField(default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=None, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    class Meta:
        ordering = ["orden"]

    def __unicode__(self):
		return unicode(self.descripcion) or u''

class Universidad(models.Model):
    descripcion = models.CharField(max_length="50", default=None, null=True, blank=True)
    nemonico = models.CharField(max_length="50", default=None, null=True, blank=True)
    pais = models.ForeignKey(Pais, default=None, null=True, blank=True)

    orden = models.IntegerField(null= True, blank= True)
    fecha_creacion = models.DateField(default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=None, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    class Meta:
        ordering = ["orden"]

    def __unicode__(self):
		return unicode(self.descripcion) or u''

class TipoCarrera(models.Model):
    descripcion = models.CharField(max_length="50", default=None, null=True, blank=True)
    total_ciclos = models.IntegerField(null= True, blank= True, verbose_name='total de ciclos')

    orden = models.IntegerField(null= True, blank= True)
    fecha_creacion = models.DateField(default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=None, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    class Meta:
        ordering = ["orden"]

    def __unicode__(self):
		return unicode(self.descripcion) or u''

class Carrera(models.Model):
    descripcion = models.CharField(max_length="50", default=None, null=True, blank=True)
    tipo_carrera = models.ForeignKey(TipoCarrera, default=None, null=True, blank=True)

    orden = models.IntegerField(null= True, blank= True)
    fecha_creacion = models.DateField(default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=None, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    class Meta:
        ordering = ["orden"]

    def __unicode__(self):
		return unicode(self.descripcion) or u''

class TipoPuesto(models.Model):
    descripcion = models.CharField(max_length="50", default=None, null=True, blank=True)

    orden = models.IntegerField(null= True, blank= True)
    fecha_creacion = models.DateField(default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=None, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    class Meta:
        ordering = ["orden"]

    def __unicode__(self):
		return unicode(self.descripcion) or u''

class CargaHoraria(models.Model):
    descripcion = models.CharField(max_length="50", default=None, null=True, blank=True)

    orden = models.IntegerField(null= True, blank= True)
    fecha_creacion = models.DateField(default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=None, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    class Meta:
        ordering = ["orden"]

    def __unicode__(self):
		return unicode(self.descripcion) or u''

class Idioma(models.Model):
    descripcion = models.CharField(max_length="50", default=None, null=True, blank=True)

    orden = models.IntegerField(null= True, blank= True)
    fecha_creacion = models.DateField(default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=None, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    class Meta:
        ordering = ["orden"]

    def __unicode__(self):
		return unicode(self.descripcion) or u''

class Conocimiento(models.Model):
    descripcion = models.CharField(max_length="50", default=None, null=True, blank=True)

    orden = models.IntegerField(null= True, blank= True)
    fecha_creacion = models.DateField(default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=None, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    class Meta:
        ordering = ["orden"]

    def __unicode__(self):
		return unicode(self.descripcion) or u''

class TipoRemuneracion(models.Model):
    descripcion = models.CharField(max_length="50", default=None, null=True, blank=True)

    orden = models.IntegerField(null= True, blank= True)
    fecha_creacion = models.DateField(default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=None, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    class Meta:
        ordering = ["orden"]

    def __unicode__(self):
		return unicode(self.descripcion) or u''

class Beneficio(models.Model):
    descripcion = models.CharField(max_length="50", default=None, null=True, blank=True)

    orden = models.IntegerField(null= True, blank= True)
    fecha_creacion = models.DateField(default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=None, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    class Meta:
        ordering = ["orden"]

    def __unicode__(self):
		return unicode(self.descripcion) or u''

class PeriodosGraduacion(models.Model):

    descripcion = models.CharField(max_length="50", default=None, null=True, blank=True)
    valor = models.IntegerField(null= True, blank= True)
    orden = models.IntegerField(null= True, blank= True)
    fecha_creacion = models.DateField(default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=None, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    class Meta:
        ordering = ["orden"]

    def __unicode__(self):
		return unicode(self.descripcion) or u''




