from django.contrib import admin
from django.db import models
from main.models import Persona, Pais, Ciudad, GradoEstudio, Universidad, Carrera, TipoPuesto, CargaHoraria, Idioma, \
    Conocimiento, TipoRemuneracion, Beneficio
from empresa.models import Empresa

# Create your models here.

class PerfilCandidato(models.Model):
    grado_estudio = models.ForeignKey(GradoEstudio,default=None, null=True, blank=True )
    universidad = models.ManyToManyField(Universidad, default=None, blank=True, verbose_name="universidad")
    carrera = models.ManyToManyField(Carrera, default=None, blank=True, verbose_name="carrera")
    idioma = models.ManyToManyField(Idioma, default=None, blank=True, verbose_name="Idioma")
    pais = models.ForeignKey(Pais, default=None, null=True, blank=True )
    ciudad = models.ForeignKey(Ciudad, default=None, null=True, blank=True )

class Oportunidad(models.Model):
    empresa = models.ForeignKey(Empresa, default=None, null=True, blank=True)
    titulo = models.CharField(max_length="100", default=None, null=True, blank=True )
    carga_horaria = models.ForeignKey(CargaHoraria,default=None,null=True, blank=True )
    pais = models.ForeignKey(Pais, default=None, null=True, blank=True )
    ciudad = models.ForeignKey(Ciudad, default=None, null=True, blank=True )
    remuneracion = models.ForeignKey(TipoRemuneracion, default=None, null=True, blank=True )
    remuneracion_min = models.CharField(max_length="50", default=None, null=True, blank=True )
    remuneracion_max = models.CharField(max_length="50", default=None, null=True, blank=True )
    fecha_cese = models.DateField(null=True)
    tipo_puesto = models.ForeignKey(TipoPuesto, default=None, null=True, blank=True, )
    beneficio = models.ForeignKey(Beneficio, default=None, null=True, blank=True)
    resumen = models.CharField(max_length="1000", default=None, null=True, blank=True )
    perfil_candidato = models.ForeignKey(PerfilCandidato, default=None, null=True, blank=True)

