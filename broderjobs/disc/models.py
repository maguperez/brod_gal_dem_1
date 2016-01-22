from django.db import models
from estudiante.models import Estudiante
from main import utils

items_registro = utils.estado_registro()
letras = []
letras.append(('D', 'D'))
letras.append(('I', 'I'))
letras.append(('S', 'S'))
letras.append(('C', 'C'))

class Pregunta(models.Model):

    descripcion = models.CharField(max_length="50", default=None, null=True, blank=True,  )
    orden = models.IntegerField(default=None, null=True, blank=True )

    usuario_creacion = models.CharField(max_length="50", default=None, null=True, blank=True)
    fecha_creacion = models.DateField(default=None, null=True, blank=True)
    usuario_modificacion = models.CharField(max_length="50", default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=None, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    def __unicode__(self):
        return unicode(self.descripcion) or u''

    class Meta:
        ordering = ["orden"]

class Respuesta(models.Model):


    pregunta = models.ForeignKey(Pregunta, default=None, null=True, blank=True)
    descripcion = models.CharField(max_length="50", default=None, null=True, blank=True,  )
    letra =  models.CharField(choices=letras, max_length=1, default='A', null=True, blank=True)
    orden = models.IntegerField(default=None, null=True, blank=True )

    usuario_creacion = models.CharField(max_length="50", default=None, null=True, blank=True)
    fecha_creacion = models.DateField(default=None, null=True, blank=True)
    usuario_modificacion = models.CharField(max_length="50", default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=None, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    class Meta:
        ordering = ["pregunta", "orden"]

    def __unicode__(self):
        return unicode(self.descripcion) or u''

class RespuestaEstudiante(models.Model):

    estudiante = models.ForeignKey(Estudiante, default=None, null=True, blank=True)
    respuesta = models.ForeignKey(Respuesta, default=None, null=True, blank=True)
    descripcion = models.CharField(max_length="50", default=None, null=True, blank=True,  )
    letra_mas =  models.CharField(choices=letras, max_length=1, default='', null=True, blank=True)
    letra_menos =  models.CharField(choices=letras, max_length=1, default='', null=True, blank=True)
    orden = models.IntegerField(default=None, null=True, blank=True )

    usuario_creacion = models.CharField(max_length="50", default=None, null=True, blank=True)
    fecha_creacion = models.DateField(default=None, null=True, blank=True)
    usuario_modificacion = models.CharField(max_length="50", default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=None, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    def __unicode__(self):
        return unicode(self.estudiante) or u''