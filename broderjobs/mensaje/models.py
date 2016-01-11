from django.db import models
from django.contrib.auth.models import User
from oportunidad.models import Postulacion, Oportunidad

from main import utils


items_registro = utils.estado_registro()
class Mensaje(models.Model):
    items_estado = utils.estado_mensaje()

    oportunidad = models.ForeignKey(Oportunidad,default=None, null=True, blank=True )
    usuario_remitente = models.ForeignKey(User,default=None, null=True, blank=True )
    asunto = models.CharField(default=None, null=True, blank=True, max_length=100)
    contenido = models.TextField(default=None, null=True, blank=True)
    permite_respuesta = models.BooleanField(default=False, blank=True)
    es_respuesta = models.IntegerField(default=None, null=True, blank=True)

    fecha_creacion = models.DateField(default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=None, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    def __unicode__(self):
        return unicode('%s' % (self.asunto)) or u''

class Mensaje_Destinatario(models.Model):

    mensaje = models.ForeignKey(Mensaje, default=None, null=True, blank=True, max_length=1000)
    usuario_destinatario = models.ForeignKey(User,default=None, null=True, blank=True)
    leido = models.BooleanField(default=False, blank=True)
    fecha_leido = models.DateField(default=None, null=True, blank=True)

    fecha_creacion = models.DateField(default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=None, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    def __unicode__(self):
        return unicode('%s' % (self.usuario_destinatario)) or u''

class Notificacion(models.Model):

    usuario_destinatario = models.ForeignKey(User,default=None, null=True, blank=True)
    oportunidad = models.ForeignKey(Oportunidad,default=None, null=True, blank=True )
    asunto = models.CharField(default=None, null=True, blank=True, max_length=100)
    fecha_leido = models.DateField(default=None, null=True, blank=True)
    es_mensaje = models.BooleanField(default=False, blank=True)

    fecha_creacion = models.DateField(default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=None, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    def __unicode__(self):
        return unicode('%s' % (self.asunto)) or u''
