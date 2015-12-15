from django.db import models
from django.contrib.auth.models import User
from main.models import Persona, Pais, Ciudad, GradoEstudio, Universidad, Carrera, TipoPuesto, CargaHoraria, Idioma,\
    Conocimiento
from main import utilitarios

items_registro = utilitarios.estado_registro()

class ImagenSilder(models.Model):
    titulo = models.CharField(max_length="50", default=None, null=True, blank=True)
    url = models.CharField(max_length="1000", default=None, null=True, blank=True)
    imagen = models.ImageField('imagen', upload_to='img/%Y/%m/%d', null=True, blank=True)

    fecha_creacion = models.DateField(default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=None, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)
    usuario_modificacion = models.ForeignKey(User, default=None, null=True, blank=True)

    def __unicode__(self):
        return self.titulo

    @property
    def set_imagen(self):
        if self.imagen:
            return self.imagen.url
        # else:
        #     return "/static/img/profile/profile_default.png"

class Sector(models.Model):
    descripcion = models.CharField(max_length="50")
    fecha_creacion = models.DateField(default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=None, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    fecha_creacion = models.DateField(default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=None, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    def __unicode__(self):
        return self.descripcion

class Puesto(models.Model):
    descripcion = models.CharField(max_length="50")

    fecha_creacion = models.DateField(default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=None, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    def __unicode__(self):
        return self.descripcion

class NumeroFuncionarios(models.Model):
    descripcion = models.CharField(max_length="50")

    fecha_creacion = models.DateField(default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=None, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    def __unicode__(self):
        return self.descripcion

class FacturacionAnual(models.Model):
    descripcion = models.CharField(max_length="50")

    fecha_creacion = models.DateField(default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=None, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    def __unicode__(self):
        return self.descripcion

class CategoriaEmpresa(models.Model):

    descripcion = models.CharField(max_length="50")

    fecha_creacion = models.DateField(default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=None, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    def __unicode__(self):
        return unicode('%s' % (self.persona)) or u''

class Empresa(models.Model):

    nombre =  models.CharField(max_length="100", default=None, null=True, blank=True )
    descripcion = models.CharField(max_length="200", default=None, null=True, blank=True )
    quienes_somos = models.CharField(max_length="1000", default=None, null=True, blank=True )
    RUC = models.CharField(max_length="20", default=None, null=True, blank=True )
    sector = models.ForeignKey(Sector, default=None, null=True, blank=True )
    numero_funcionarios = models.ForeignKey(NumeroFuncionarios, default=None, null=True, blank=True)
    facturacion_anual = models.ForeignKey(FacturacionAnual, default=None, null=True, blank=True)
    ano_fundacion =  models.CharField(max_length="10", default=None, null=True, blank=True )
    pais = models.ForeignKey(Pais, default=None, null=True, blank=True )
    ciudad = models.ForeignKey(Ciudad, default=None, null=True, blank=True )
    website = models.CharField(max_length="50", default=None, null=True, blank=True )
    logo = models.ImageField('logo', upload_to='img/%Y/%m/%d', null=True, blank=True)
    imagen_slider = models.ManyToManyField(ImagenSilder, default=None, blank=True, verbose_name="Imagenes")
    direccion_map = models.CharField(max_length="100", default=None, null=True, blank=True)
    longitud = models.FloatField(verbose_name='longitud', default=None, null=True, blank=True )
    latitud = models.FloatField(verbose_name='latitud', default=None, null=True, blank=True )


    fecha_creacion = models.DateField(default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=None, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)
    usuario_modificacion = models.ForeignKey(User, default=None, null=True, blank=True)


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

    fecha_creacion = models.DateField(default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=None, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    def __unicode__(self):
        return unicode('%s' % (self.persona)) or u''

class EvaluacionEmpresa(models.Model):

    empresa = models.ForeignKey(Empresa)
    usuario = models.ForeignKey(User)
    linea_carrera = models.FloatField(default=None, null=True, blank=True )
    flexibilidad_horarios = models.FloatField(default=None, null=True, blank=True )
    ambiente_trabajo = models.FloatField(default=None, null=True, blank=True )
    salarios = models.FloatField(default=None, null=True, blank=True )
    ranking = models.FloatField(default=None, null=True, blank=True )
    fecha_creacion = models.DateField(default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=None, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    def __unicode__(self):
        return unicode('%s' % (self.empresa)) or u''

class RankingEmpresa(models.Model):

    empresa = models.ForeignKey(Empresa)
    linea_carrera = models.FloatField(default=None, null=True, blank=True )
    flexibilidad_horarios = models.FloatField(default=None, null=True, blank=True )
    ambiente_trabajo = models.FloatField(default=None, null=True, blank=True )
    salarios = models.FloatField(default=None, null=True, blank=True )
    ranking_general = models.FloatField(default=None, null=True, blank=True )
    fecha_creacion = models.DateField(default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=None, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    def __unicode__(self):
        return unicode('%s' % (self.empresa)) or u''


