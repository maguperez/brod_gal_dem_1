from django.db import models
from django.contrib.auth.models import User
from main.models import Persona, Pais, Ciudad, GradoEstudio, Universidad, Carrera, TipoPuesto, CargaHoraria, Idioma,\
    Conocimiento
from main import utils
from datetime import date, datetime
from broderjobs.settings import STATIC_URL

items_registro = utils.estado_registro()


class Sector(models.Model):
    descripcion = models.CharField(max_length="50")
    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)
    orden = models.IntegerField(null= True, blank= True)

    class Meta:
        ordering = ["orden"]

    def __unicode__(self):
        return self.descripcion

class Puesto(models.Model):
    descripcion = models.CharField(max_length="50")

    orden = models.IntegerField(null= True, blank= True)
    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    class Meta:
        ordering = ["orden"]

    def __unicode__(self):
        return self.descripcion

class NumeroFuncionarios(models.Model):
    descripcion = models.CharField(max_length="50")

    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)
    orden = models.IntegerField(null= True, blank= True)
    class Meta:
        ordering = ["orden"]

    def __unicode__(self):
        return self.descripcion

class FacturacionAnual(models.Model):
    descripcion = models.CharField(max_length="50")

    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)
    orden = models.IntegerField(null= True, blank= True)
    class Meta:
        ordering = ["orden"]

    def __unicode__(self):
        return self.descripcion

class CategoriaEmpresa(models.Model):

    descripcion = models.CharField(max_length="50")

    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)
    orden = models.IntegerField(null= True, blank= True)
    class Meta:
        ordering = ["orden"]

    def __unicode__(self):
        return unicode('%s' % (self.persona)) or u''

class Empresa(models.Model):

    nombre =  models.CharField(max_length="100", default=None, null=True, blank=True )
    descripcion = models.CharField(max_length="200", default=None, null=True, blank=True )
    quienes_somos = models.CharField(max_length="1000", default=None, null=True, blank=True )
    telefono = models.CharField(max_length="100", default=None, null=True, blank=True )
    RUC = models.CharField(max_length="20", default=None, null=True, blank=True )
    sector = models.ForeignKey(Sector, default=None, null=True, blank=True )
    numero_funcionarios = models.ForeignKey(NumeroFuncionarios, default=None, null=True, blank=True)
    facturacion_anual = models.ForeignKey(FacturacionAnual, default=None, null=True, blank=True)
    ano_fundacion =  models.CharField(max_length="10", default=None, null=True, blank=True )
    pais = models.ForeignKey(Pais, default=None, null=True, blank=True )
    ciudad = models.ForeignKey(Ciudad, default=None, null=True, blank=True )
    website = models.CharField(max_length="50", default=None, null=True, blank=True )
    logo = models.ImageField('logo', upload_to='img/%Y/%m/%d', null=True, blank=True)
    direccion_map = models.CharField(max_length="100", default=None, null=True, blank=True)
    longitud = models.FloatField(verbose_name='longitud', default=None, null=True, blank=True )
    latitud = models.FloatField(verbose_name='latitud', default=None, null=True, blank=True )

    usuario_creacion = models.CharField(max_length="50", default=None, null=True, blank=True)
    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    usuario_modificacion = models.CharField(max_length="50", default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)


    def __unicode__(self):
        return '%s' % (self.nombre)

    @property
    def set_logo(self):
        if self.logo:
            return self.logo.url
        else:
            return STATIC_URL+"img/profile/profile_default.png"

class Representante(models.Model):

    persona = models.OneToOneField(Persona)
    empresa = models.ForeignKey(Empresa)
    administrador = models.BooleanField(default=False, blank=True)

    usuario_creacion = models.CharField(max_length="50", default=None, null=True, blank=True)
    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    usuario_modificacion = models.CharField(max_length="50", default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    def __unicode__(self):
        return unicode(self.persona) or u''

class EvaluacionEmpresa(models.Model):

    empresa = models.ForeignKey(Empresa)
    usuario = models.ForeignKey(User)
    linea_carrera = models.FloatField(default=None, null=True, blank=True )
    flexibilidad_horarios = models.FloatField(default=None, null=True, blank=True )
    ambiente_trabajo = models.FloatField(default=None, null=True, blank=True )
    salarios = models.FloatField(default=None, null=True, blank=True )
    ranking = models.FloatField(default=None, null=True, blank=True )

    usuario_creacion = models.CharField(max_length="50", default=None, null=True, blank=True)
    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    usuario_modificacion = models.CharField(max_length="50", default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    def __unicode__(self):
        return unicode((self.empresa)) or u''

class RankingEmpresa(models.Model):

    empresa = models.ForeignKey(Empresa)
    linea_carrera = models.FloatField(default=None, null=True, blank=True )
    flexibilidad_horarios = models.FloatField(default=None, null=True, blank=True )
    ambiente_trabajo = models.FloatField(default=None, null=True, blank=True )
    salarios = models.FloatField(default=None, null=True, blank=True )
    ranking_general = models.FloatField(default=None, null=True, blank=True )

    usuario_creacion = models.CharField(max_length="50", default=None, null=True, blank=True)
    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    usuario_modificacion = models.CharField(max_length="50", default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    def __unicode__(self):
        return unicode('%s' % (self.empresa)) or u''

class Empresa_Imagenes(models.Model):

    empresa = models.ForeignKey(Empresa, default=None, null=True, blank=True)
    file = models.ImageField(upload_to='img/%Y/%m/%d', default=None, null=True, blank=True)
    slug = models.SlugField(max_length=50, blank=True)

    usuario_creacion = models.CharField(max_length="50", default=None, null=True, blank=True)
    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    usuario_modificacion = models.CharField(max_length="50", default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    def __unicode__(self):
        return self.file.name

    @models.permalink
    def get_absolute_url(self):
        return ('upload-new', )

    def save(self, *args, **kwargs):
        self.slug = self.file.name
        super(Empresa_Imagenes, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """delete -- Remove to leave file."""
        self.file.delete(False)
        super(Empresa_Imagenes, self).delete(*args, **kwargs)

    # @property
    # def set_imagen(self):
    #     if self.imagen:
    #         return self.imagen.url
    #     else:
    #         return "/static/img/profile/profile_default.png"

class Picture(models.Model):
    """This is a small demo using just two fields. The slug field is really not
    necessary, but makes the code simpler. ImageField depends on PIL or
    pillow (where Pillow is easily installable in a virtualenv. If you have
    problems installing pillow, use a more generic FileField instead.

    """
    file = models.ImageField(upload_to="pictures")
    slug = models.SlugField(max_length=50, blank=True)
    empresa = models.ForeignKey(Empresa, default=None, null=True, blank=True)

    def __unicode__(self):
        return self.slug

    @models.permalink
    def get_absolute_url(self):
        return ('upload-new', )

    def save(self, *args, **kwargs):
        self.slug = self.file.name
        super(Picture, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """delete -- Remove to leave file."""
        self.file.delete(False)
        super(Picture, self).delete(*args, **kwargs)

    @property
    def set_imagen(self):
        if self.file:
            return self.file.url
        else:
            return "/static/img/profile/profile_default.png"

class VideoUrl(models.Model):

    url = models.URLField(default=None, null=True, blank=True)
    empresa = models.ForeignKey(Empresa, default=None, null=True, blank=True)

    def __unicode__(self):
        return self.url

class EmpresaRedesSociales(models.Model):

    empresa = models.ForeignKey(Empresa)
    facebook = models.CharField(max_length="200", default=None, null=True, blank=True)
    twitter = models.CharField(max_length="200", default=None, null=True, blank=True)
    linkedin =  models.CharField(max_length="200", default=None, null=True, blank=True)


    usuario_creacion = models.CharField(max_length="50", default=None, null=True, blank=True)
    fecha_creacion = models.DateField(default=datetime.now, null=True, blank=True)
    usuario_modificacion = models.CharField(max_length="50", default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=datetime.now, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    def __unicode__(self):
        return unicode('%s' % (self.empresa)) or u''



