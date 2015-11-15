# coding=utf-8
from django.db import models
from django.contrib.postgres.fields import ArrayField
from main.models import Persona, Pais, Ciudad, GradoEstudio, Universidad, Carrera, TipoPuesto, CargaHoraria, Idioma, Conocimiento
from empresa.models import Empresa, Puesto
from main import utilitarios


class Estudiante(models.Model):
    items_semestre = utilitarios.semestre_rango()
    items_anos = utilitarios.anos_rango()

    persona = models.OneToOneField(Persona)
    grado_estudio = models.ForeignKey(GradoEstudio,default=None, null=True, blank=True )
    universidad = models.ForeignKey(Universidad,default=None, null=True, blank=True )
    carrera = models.ForeignKey(Carrera, default=None, null=True, blank=True )
    semestre_inicio_estudio = models.CharField(choices=items_semestre,max_length=2, default=None, null=True, blank=True)
    ano_inicio_estudio = models.CharField(choices=items_anos, max_length=4, default=None, null=True,  blank=True, )
    semestre_graduacion = models.CharField(choices=items_semestre, max_length=2, default=None, null=True, blank=True, )
    ano_graduacion= models.CharField(choices=items_anos, max_length=4, default=None, null=True, blank=True)
    pais = models.ForeignKey(Pais, default=None, null=True, blank=True )
    ciudad = models.ForeignKey(Ciudad, default=None, null=True, blank=True )
    carga_horaria = models.ForeignKey(CargaHoraria, null=True)
    tipo_puesto = models.ManyToManyField(TipoPuesto, default=None, blank=True, verbose_name="Tipo Puesto")
    foto = models.ImageField('foto perfil', upload_to='img/%Y/%m/%d', null=True, blank=True)

    def __unicode__(self):
		return unicode('%s' % (self.persona)) or u''

    @property
    def set_foto(self):
        if self.foto:
            return self.foto.url
        else:
            return "/static/img/profile/profile_default.png"


class Resumen(models.Model):
    estudiante =  models.ForeignKey(Estudiante)
    descripcion = models.CharField(max_length="100", default=None, null=True, blank=True)

    def __unicode__(self):
		return unicode('%s' % (self.estudiante)) or u''

class ActividadesExtra(models.Model):
    estudiante =  models.ForeignKey(Estudiante)
    descripcion = models.CharField(max_length="50", default=None, null=True, blank=True)
    organizacion = models.CharField(max_length="50", default=None, null=True, blank=True)

    def __unicode__(self):
		return self.descripcion

class ExperienciaProfesional(models.Model):
    estudiante =  models.ForeignKey(Estudiante)
    puesto = models.ForeignKey(Puesto)
    empresa = models.ForeignKey(Empresa, default=None, null=True, blank=True)
    fecha_desde = models.DateField(null=True)
    fecha_hasta = models.DateField(default=None, null=True, blank=True)
    trabajo_actual = models.CharField(max_length=1, default='N',)
    descripcion = models.CharField(max_length="100", default=None, null=True)

    def __unicode__(self):
		return self.descripcion

class Voluntariado(models.Model):
    estudiante =  models.ForeignKey(Estudiante)
    cargo = models.CharField(max_length="50", default=None, null=True, blank=True)
    organizacion = models.CharField(max_length="50", default=None, null=True, blank=True)
    fecha_desde = models.DateField(null=True)
    fecha_hasta = models.DateField(default=None, null=True, blank=True)
    voluntariado_actual = models.CharField(max_length=1, default='N')
    descripcion = models.CharField(max_length="100", default=None, null=True, blank=True)

    def __unicode__(self):
		return self.descripcion

class EstudianteIdioma(models.Model):
    estudiante =  models.ForeignKey(Estudiante)
    idioma =  models.ForeignKey(Idioma)

    def __unicode__(self):
		return '%s' % (self.estudiante)

class EstudianteConocimiento(models.Model):
    estudiante =  models.ForeignKey(Estudiante)
    conocimiento =  models.ForeignKey(Conocimiento)

    def __unicode__(self):
		return self.estudiante.persona