from django.db import models
from django.contrib.auth.models import User
from oportunidad.models import Postulacion

from main import utilitarios


items_registro = utilitarios.estado_registro()
class Mensaje(models.Model):
    items_estado = utilitarios.estado_mensaje()

    postulacion = models.ForeignKey(Postulacion,default=None, null=True, blank=True )
    usuario_remitente = models.ForeignKey(User,default=None, null=True, blank=True )
    asunto = models.CharField(default=None, null=True, blank=True, max_length=100)
    contenido = models.CharField(default=None, null=True, blank=True, max_length=1000)
    permite_respuesta = models.BooleanField(default=False, blank=True)
    es_respuesta = models.IntegerField(default=None, null=True, blank=True)

    fecha_creacion = models.DateField(default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=None, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

class Mensaje_Destinatario(models.Model):
    items_estado = utilitarios.estado_mensaje()

    mensaje = models.ForeignKey(Mensaje, default=None, null=True, blank=True, max_length=1000)
    usuario_destinatario = models.ForeignKey(User,default=None, null=True, blank=True)
    leido = models.BooleanField(default=False, blank=True)
    fecha_leido = models.DateField(default=None, null=True, blank=True)

    fecha_creacion = models.DateField(default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=None, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)
