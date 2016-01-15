from django.contrib import admin
from django.db import models
from main.models import Persona, Pais, Ciudad, GradoEstudio, Universidad, Carrera, TipoPuesto, CargaHoraria, Idioma, \
    Conocimiento, TipoRemuneracion, Beneficio, PeriodosGraduacion
from empresa.models import Empresa
from estudiante.models import Estudiante
from django.contrib.auth.models import User

from main import utils
items_registro = utils.estado_registro()

class ProcesoFase(models.Model):

    descripcion = models.CharField(max_length="50", default=None, null=True, blank=True,  )
    orden = models.IntegerField(default=None, null=True, blank=True )
    mensaje_contenido = models.TextField(default=None, null=True, blank=True,  )
    mensaje_asunto = models.CharField(max_length="100", default=None, null=True, blank=True,  )

    usuario_creacion = models.CharField(max_length="50", default=None, null=True, blank=True)
    fecha_creacion = models.DateField(default=None, null=True, blank=True)
    usuario_modificacion = models.CharField(max_length="50", default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=None, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    def __unicode__(self):
		return unicode(self.descripcion) or u''

class Oportunidad(models.Model):
    items_estado = utils.estado_oportunidad()
    periodo= []
    for e in PeriodosGraduacion.objects.all():
        periodo.append((str(e.id), e.descripcion))

    empresa = models.ForeignKey(Empresa, default=None, null=True, blank=True)
    titulo = models.CharField(max_length="100", default=None, null=True, blank=True )
    carga_horaria = models.ForeignKey(CargaHoraria, default=None, null=True, blank=True, verbose_name="Jornada Laboral" )
    pais = models.ForeignKey(Pais, null=True, blank=True )
    ciudad = models.ForeignKey(Ciudad, null=True, blank=True )
    ciudad = models.ForeignKey(Ciudad, null=True, blank=True )
    remuneracion = models.ForeignKey(TipoRemuneracion, default=None, null=True, blank=True, verbose_name="Remuneracion")
    remuneracion_min = models.CharField(max_length="50", default=None, null=True, blank=True,  )
    remuneracion_max = models.CharField(max_length="50", default=None, null=True, blank=True )
    tipo_puesto = models.ForeignKey(TipoPuesto,default=None, null=True, blank=True, verbose_name="Tipo Puesto")
    beneficio = models.ManyToManyField(Beneficio, default=None, blank=True, verbose_name="Beneficios")
    resumen = models.CharField(max_length="1000", default=None, null=True, blank=True )
    estado_oportunidad =  models.CharField(choices=items_estado, max_length=1, default=None, null=True, blank=True)
    direccion_map = models.CharField(max_length="100", default=None, null=True, blank=True)
    longitud = models.FloatField(verbose_name='longitud', default=None, null=True, blank=True )
    latitud = models.FloatField(verbose_name='latitud', default=None, null=True, blank=True )
    grado_estudio = models.ForeignKey(GradoEstudio,default=None, null=True, blank=True, verbose_name="grado estudios")
    universidad = models.ManyToManyField(Universidad, default=None, blank=True, verbose_name="universidad")
    carrera = models.ManyToManyField(Carrera, default=None, blank=True, verbose_name="carrera")
    idioma = models.ManyToManyField(Idioma, default=None, blank=True, verbose_name="Idioma")
    conocimiento = models.ManyToManyField(Conocimiento, default=None, blank=True, verbose_name="Conocimiento")
    direccion_map = models.CharField(max_length="100", default=None, null=True, blank=True)
    longitud = models.FloatField(verbose_name='longitud', default=None, null=True, blank=True )
    latitud = models.FloatField(verbose_name='latitud', default=None, null=True, blank=True )
    fecha_publicacion = models.DateField(default=None,null=True, blank=True)
    fecha_cese = models.DateField(default=None,null=True, blank=True )
    graduacion_desde = models.CharField(choices=periodo, max_length=1, default=None, null=True, blank=True)
    graduacion_hasta = models.CharField(choices=periodo, max_length=1, default=None, null=True, blank=True)
    fase = models.ForeignKey(ProcesoFase, default=None, null=True, blank=True)

    usuario_creacion = models.CharField(max_length="50", default=None, null=True, blank=True)
    fecha_creacion = models.DateField(default=None, null=True, blank=True)
    usuario_modificacion = models.CharField(max_length="50", default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=None, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)


    def __unicode__(self):
		return unicode(self.titulo) or u''

class Postulacion(models.Model):
    items_estado = utils.estado_postulacion()

    oportunidad = models.ForeignKey(Oportunidad, default=None, null=True, blank=True)
    estudiante = models.ForeignKey(Estudiante, default=None, null=True, blank=True)
    estado_postulacion =  models.CharField(choices=items_estado, max_length=1, default='A', null=True, blank=True)
    fase = models.ForeignKey(ProcesoFase, default=None, null=True, blank=True)
    estado_fase =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    usuario_creacion = models.CharField(max_length="50", default=None, null=True, blank=True)
    fecha_creacion = models.DateField(default=None, null=True, blank=True)
    usuario_modificacion = models.CharField(max_length="50", default=None, null=True, blank=True)
    fecha_modificacion = models.DateField(default=None, null=True, blank=True)
    estado =  models.CharField(choices=items_registro, max_length=1, default='A', null=True, blank=True)

    def __unicode__(self):
		return unicode(self.estudiante) or u''



