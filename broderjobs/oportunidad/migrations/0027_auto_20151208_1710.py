# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20151208_1639'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('empresa', '0012_auto_20151203_1517'),
        ('oportunidad', '0026_auto_20151208_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='oportunidad',
            name='beneficio',
            field=models.ManyToManyField(default=None, to='main.Beneficio', verbose_name=b'Beneficios', blank=True),
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='carga_horaria',
            field=models.ForeignKey(default=None, blank=True, to='main.CargaHoraria', null=True, verbose_name=b'Jornada Laboral'),
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='carrera',
            field=models.ManyToManyField(default=None, to='main.Carrera', verbose_name=b'carrera', blank=True),
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='ciudad',
            field=models.ForeignKey(blank=True, to='main.Ciudad', null=True),
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='conocimiento',
            field=models.ManyToManyField(default=None, to='main.Conocimiento', verbose_name=b'Conocimiento', blank=True),
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='direccion_map',
            field=models.CharField(default=None, max_length=b'100', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='empresa',
            field=models.ForeignKey(default=None, blank=True, to='empresa.Empresa', null=True),
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='estado',
            field=models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')]),
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='estado_opotunidad',
            field=models.CharField(default=None, max_length=1, null=True, blank=True, choices=[(b'P', b'Pendiente'), (b'A', b'Abierto'), (b'C', b'Cerrado')]),
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='fecha_cese',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='fecha_creacion',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='fecha_modificacion',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='fecha_publicacion',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='grado_estudio',
            field=models.ForeignKey(default=None, blank=True, to='main.GradoEstudio', null=True, verbose_name=b'grado estudios'),
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='graduacion_desde',
            field=models.CharField(default=None, max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='graduacion_hasta',
            field=models.CharField(default=None, max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='idioma',
            field=models.ManyToManyField(default=None, to='main.Idioma', verbose_name=b'Idioma', blank=True),
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='latitud',
            field=models.FloatField(default=None, null=True, verbose_name=b'latitud', blank=True),
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='longitud',
            field=models.FloatField(default=None, null=True, verbose_name=b'longitud', blank=True),
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='pais',
            field=models.ForeignKey(blank=True, to='main.Pais', null=True),
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='remuneracion',
            field=models.ForeignKey(default=None, blank=True, to='main.TipoRemuneracion', null=True, verbose_name=b'Remuneracion'),
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='remuneracion_max',
            field=models.CharField(default=None, max_length=b'50', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='remuneracion_min',
            field=models.CharField(default=None, max_length=b'50', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='resumen',
            field=models.CharField(default=None, max_length=b'1000', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='tipo_puesto',
            field=models.ForeignKey(default=None, blank=True, to='main.TipoPuesto', null=True, verbose_name=b'Tipo Puesto'),
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='universidad',
            field=models.ManyToManyField(default=None, to='main.Universidad', verbose_name=b'universidad', blank=True),
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='usuario',
            field=models.ForeignKey(default=None, blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
