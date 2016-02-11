from django.db import models
from estudiante.models import Estudiante
from main import utils
from datetime import date, datetime

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

class EstudianteRespuestas(models.Model):

    estudiante = models.ForeignKey(Estudiante, default=None, null=True, blank=True)
    pregunta = models.ForeignKey(Pregunta, default=None, null=True, blank=True)
    descripcion = models.CharField(max_length="200", default=None, null=True, blank=True,  )
    letra_mas =  models.CharField(choices=letras, max_length=1, default='', null=True, blank=True)
    letra_menos =  models.CharField(choices=letras, max_length=1, default='', null=True, blank=True)
    orden = models.IntegerField(default=None, null=True, blank=True )

    usuario_creacion = models.CharField(max_length="50", default=None, null=True, blank=True)
    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    usuario_modificacion = models.CharField(max_length="50", default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    def __unicode__(self):
        return unicode(self.estudiante) or u''
    class Meta:
        ordering = ["estudiante","pregunta", "orden"]

class DiscCodificacion(models.Model):

    letra =  models.CharField(choices=letras, max_length=1, default='', null=True, blank=True)
    valor_desde = models.IntegerField(default=None, null=True, blank=True)
    valor_hasta = models.IntegerField(default=None, null=True, blank=True)
    segmento = models.IntegerField(default=None, null=True, blank=True, )
    orden = models.IntegerField(default=None, null=True, blank=True, )

    usuario_creacion = models.CharField(max_length="50", default=None, null=True, blank=True)
    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    usuario_modificacion = models.CharField(max_length="50", default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    def __unicode__(self):
        return unicode(self.letra) or u''
    class Meta:
        ordering = ["letra","valor_desde", "valor_hasta" ,"segmento","orden"]

class Perfil(models.Model):

    descripcion = models.TextField(default=None, null=True, blank=True, )
    no_concluyente = models.BooleanField(default=False, blank=True)
    orden = models.IntegerField(default=None, null=True, blank=True )

    usuario_creacion = models.CharField(max_length="50", default=None, null=True, blank=True)
    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    usuario_modificacion = models.CharField(max_length="50", default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    def __unicode__(self):
        return unicode(self.descripcion) or u''

    class Meta:
        ordering = ["orden"]

class PatronPerfil(models.Model):

    perfil = models.ForeignKey(Perfil, default=None, null=True, blank=True)
    nro_patron = models.CharField(max_length="50", default=None, null=True, blank=True,  )
    orden = models.IntegerField(default=None, null=True, blank=True )

    usuario_creacion = models.CharField(max_length="50", default=None, null=True, blank=True)
    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    usuario_modificacion = models.CharField(max_length="50", default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    def __unicode__(self):
        return unicode(self.perfil) or u''

    class Meta:
        ordering = ["orden"]

class EstudiantePatron(models.Model):

    estudiante = models.ForeignKey(Estudiante, default=None, null=True, blank=True)
    patron_perfil = models.ForeignKey(PatronPerfil, default=None, null=True, blank=True)

    total_d = models.IntegerField(default=None, null=True, blank=True )
    total_i = models.IntegerField(default=None, null=True, blank=True )
    total_s = models.IntegerField(default=None, null=True, blank=True )
    total_c = models.IntegerField(default=None, null=True, blank=True )
    patron = models.CharField(max_length="50", default=None, null=True, blank=True)

    orden = models.IntegerField(default=None, null=True, blank=True )

    usuario_creacion = models.CharField(max_length="50", default=None, null=True, blank=True)
    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    usuario_modificacion = models.CharField(max_length="50", default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    def __unicode__(self):
        return unicode(self.estudiante) or u''

    class Meta:
        ordering = ["estudiante"]