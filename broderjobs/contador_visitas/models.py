# coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from main.models import Persona, Pais, Ciudad, GradoEstudio, Universidad, Carrera, TipoPuesto, CargaHoraria, Idioma, Conocimiento
from oportunidad.models import Oportunidad
from main import utils

items_registro = utils.estado_registro()
class VisitasOportunidad(models.Model):

    oportunidad = models.ForeignKey(Oportunidad, default=None, null=True, blank=True)
    ip = models.CharField(max_length="100", default=None, null=True, blank=True)

    usuario_creacion = models.CharField(max_length="50", default=None, null=True, blank=True)
    fecha_creacion = models.DateField(default=None, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    def __unicode__(self):
        return unicode(self.id) or u''