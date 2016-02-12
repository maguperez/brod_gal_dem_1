from django.db import models
from estudiante.models import Estudiante
from empresa.models import Empresa
from main import utils
from datetime import date, datetime

items_registro = utils.estado_registro()
letras = []
letras.append(('D', 'D'))
letras.append(('I', 'I'))
letras.append(('S', 'S'))
letras.append(('C', 'C'))

# Create your models here.
class PerfilCultura(models.Model):

    nombre = models.CharField(max_length="50", default=None, null=True, blank=True,  )
    descripcion = models.TextField(default=None, null=True, blank=True,  )
    orden = models.IntegerField(default=None, null=True, blank=True )

    usuario_creacion = models.CharField(max_length="50", default=None, null=True, blank=True)
    fecha_creacion = models.DateField(default=None, null=True, blank=True)
    usuario_modificacion = models.CharField(max_length="50", default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=None, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    def __unicode__(self):
        return unicode(self.nombre) or u''

    class Meta:
        ordering = ["orden"]

class PreguntaCultura(models.Model):

    descripcion = models.TextField(default=None, null=True, blank=True,  )

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

class RespuestaCultura(models.Model):

    pregunta = models.ForeignKey(PreguntaCultura, default=None, null=True, blank=True)
    descripcion = models.TextField(default=None, null=True, blank=True,  )
    perfil_cultura= models.ForeignKey(PerfilCultura, default=None, null=True, blank=True)

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

class CulturaMatrizDISC(models.Model):

    perfil_cultura = models.ForeignKey(PerfilCultura, default=None, null=True, blank=True)
    letra_d =  models.IntegerField(default=None, null=True, blank=True)
    letra_i =  models.IntegerField(default=None, null=True, blank=True)
    letra_s =  models.IntegerField(default=None, null=True, blank=True)
    letra_c =  models.IntegerField(default=None, null=True, blank=True)
    resultado = models.IntegerField(default=None, null=True, blank=True )

    orden = models.IntegerField(default=None, null=True, blank=True )
    usuario_creacion = models.CharField(max_length="50", default=None, null=True, blank=True)
    fecha_creacion = models.DateField(default=None, null=True, blank=True)
    usuario_modificacion = models.CharField(max_length="50", default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=None, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    class Meta:
        ordering = ["perfil_cultura"]

    def __unicode__(self):
        return unicode(self.perfil_cultura) or u''

class EmpresaRespuestas(models.Model):

    empresa = models.ForeignKey(Empresa, default=None, null=True, blank=True)
    pregunta = models.ForeignKey(PreguntaCultura, default=None, null=True, blank=True)
    respuesta = models.ForeignKey(RespuestaCultura, default=None, null=True, blank=True)
    orden = models.IntegerField(default=None, null=True, blank=True )

    usuario_creacion = models.CharField(max_length="50", default=None, null=True, blank=True)
    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    usuario_modificacion = models.CharField(max_length="50", default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    def __unicode__(self):
        return unicode(self.empresa) or u''

    class Meta:
        ordering = ["empresa","pregunta", "orden"]

class EmpresaCultura(models.Model):

    empresa = models.ForeignKey(Empresa, default=None, null=True, blank=True)
    porcentaje_clan = models.FloatField(default=None, null=True, blank=True )
    porcentaje_adhocracia = models.FloatField(default=None, null=True, blank=True )
    porcentaje_jerarquico = models.FloatField(default=None, null=True, blank=True )
    porcentaje_racional = models.FloatField(default=None, null=True, blank=True )


    orden = models.IntegerField(default=None, null=True, blank=True )
    usuario_creacion = models.CharField(max_length="50", default=None, null=True, blank=True)
    fecha_creacion = models.DateField(default=None, null=True, blank=True)
    usuario_modificacion = models.CharField(max_length="50", default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=None, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    class Meta:
        ordering = ["empresa"]

    def __unicode__(self):
        return unicode(self.empresa) or u''
