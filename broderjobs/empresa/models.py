from django.db import models
from main.models import Persona, Pais, Ciudad, GradoEstudio, Universidad, Carrera, TipoPuesto, CargaHoraria, Idioma, Conocimiento


class Sector(models.Model):
    descripcion = models.CharField(max_length="50")

    def __unicode__(self):
        return self.descripcion


class Puesto(models.Model):
    descripcion = models.CharField(max_length="50")

    def __unicode__(self):
        return self.descripcion

class NumeroFuncionarios(models.Model):
    descripcion = models.CharField(max_length="50")

    def __unicode__(self):
        return self.descripcion

class FacturacionAnual(models.Model):
    descripcion = models.CharField(max_length="50")

    def __unicode__(self):
        return self.descripcion

class Empresa(models.Model):

    nombre =  models.CharField(max_length="100", default=None, null=True, blank=True )
    descripcion = models.CharField(max_length="1000", default=None, null=True, blank=True )
    RUC = models.CharField(max_length="20", default=None, null=True, blank=True )
    sector = models.ForeignKey(Sector, default=None, null=True, blank=True )
    numero_funcionarios = models.ForeignKey(NumeroFuncionarios, default=None, null=True, blank=True)
    facturacion_anual = models.ForeignKey(FacturacionAnual, default=None, null=True, blank=True)
    ano_fundacion =  models.CharField(max_length="10", default=None, null=True, blank=True )
    pais = models.ForeignKey(Pais, default=None, null=True, blank=True )
    ciudad = models.ForeignKey(Ciudad, default=None, null=True, blank=True )
    website = models.CharField(max_length="50", default=None, null=True, blank=True )
    logo = models.ImageField('logo', upload_to='img/%Y/%m/%d', null=True, blank=True)

    def __unicode__(self):
        return '%s' % (self.nombre)

    @property
    def set_logo(self):
        if self.logo:
            return self.logo.url
        else:
            return "/static/img/profile/profile_default.png"

class Representante(models.Model):

    persona = models.OneToOneField(Persona)
    empresa = models.ForeignKey(Empresa)

    def __unicode__(self):
        return unicode('%s' % (self.persona)) or u''


