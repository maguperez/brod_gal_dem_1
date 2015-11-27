from django.contrib import admin
from django.db import models
from main.models import Persona, Pais, Ciudad, GradoEstudio, Universidad, Carrera, TipoPuesto, CargaHoraria, Idioma, \
    Conocimiento, TipoRemuneracion, Beneficio
from empresa.models import Empresa
from main import utilitarios

# Create your models here.

class Oportunidad(models.Model):
    items_estado = utilitarios.estado_oportunidad()

    empresa = models.ForeignKey(Empresa, default=None, null=True, blank=True)
    titulo = models.CharField(max_length="100", default=None, null=True, blank=True )
    carga_horaria = models.ForeignKey(CargaHoraria, default=None, null=True, blank=True, verbose_name="Jornada Laboral" )
    pais = models.ForeignKey(Pais, null=True, blank=True )
    ciudad = models.ForeignKey(Ciudad, null=True, blank=True )
    remuneracion = models.ForeignKey(TipoRemuneracion, default=None, null=True, blank=True, verbose_name="Remuneracion")
    remuneracion_min = models.CharField(max_length="50", default=None, null=True, blank=True,  )
    remuneracion_max = models.CharField(max_length="50", default=None, null=True, blank=True )
    fecha_cese = models.DateField(default=None,null=True, blank=True )
    tipo_puesto = models.ForeignKey(TipoPuesto,default=None, null=True, blank=True, verbose_name="Tipo Puesto")
    beneficio = models.ManyToManyField(Beneficio, default=None, blank=True, verbose_name="Beneficios")
    resumen = models.CharField(max_length="1000", default=None, null=True, blank=True )
    estado =  models.CharField(choices=items_estado, max_length=1, default=None, null=True, blank=True)
    direccion_map = models.CharField(max_length="100", default=None, null=True, blank=True)
    longitud = models.FloatField(verbose_name='longitud', default=None, null=True, blank=True )
    latitud = models.FloatField(verbose_name='latitud', default=None, null=True, blank=True )
    grado_estudio = models.ForeignKey(GradoEstudio,default=None, null=True, blank=True, verbose_name="grado estudios")
    universidad = models.ManyToManyField(Universidad, default=None, blank=True, verbose_name="universidad")
    carrera = models.ManyToManyField(Carrera, default=None, blank=True, verbose_name="carrera")
    idioma = models.ManyToManyField(Idioma, default=None, blank=True, verbose_name="Idioma")
    conocimiento = models.ManyToManyField(Conocimiento, default=None, blank=True, verbose_name="Conocimiento")

    def __unicode__(self):
		return unicode(self.titulo) or u''

