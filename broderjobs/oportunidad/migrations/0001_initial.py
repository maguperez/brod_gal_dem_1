# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0001_initial'),
        ('main', '0001_initial'),
        ('estudiante', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BeneficioExtra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('orden', models.IntegerField(null=True, blank=True)),
                ('fecha_creacion', models.DateField(default=None, null=True, blank=True)),
                ('fecha_modificacion', models.DateField(default=None, null=True, blank=True)),
                ('estado', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')])),
            ],
            options={
                'ordering': ['orden'],
            },
        ),
        migrations.CreateModel(
            name='Oportunidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(default=None, max_length=b'100', null=True, blank=True)),
                ('remuneracion_min', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('remuneracion_max', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('resumen', models.CharField(default=None, max_length=b'1000', null=True, blank=True)),
                ('estado_oportunidad', models.CharField(default=None, max_length=1, null=True, blank=True, choices=[(b'P', b'Archivado'), (b'A', b'Abierto'), (b'C', b'Cerrado')])),
                ('direccion_map', models.CharField(default=None, max_length=b'100', null=True, blank=True)),
                ('longitud', models.FloatField(default=None, null=True, verbose_name=b'longitud', blank=True)),
                ('latitud', models.FloatField(default=None, null=True, verbose_name=b'latitud', blank=True)),
                ('fecha_publicacion', models.DateField(default=None, null=True, blank=True)),
                ('fecha_cese', models.DateField(default=None, null=True, blank=True)),
                ('edad_desde', models.IntegerField(default=None, null=True, blank=True)),
                ('edad_hasta', models.IntegerField(default=None, null=True, blank=True)),
                ('genero', models.CharField(default=b'', max_length=1, null=True, blank=True, choices=[(b'M', b'Masculino'), (b'F', b'Femenino')])),
                ('usuario_creacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_creacion', models.DateField(default=None, null=True, blank=True)),
                ('usuario_modificacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_modificacion', models.DateField(default=None, null=True, blank=True)),
                ('estado', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')])),
                ('beneficio', models.ManyToManyField(default=None, to='main.Beneficio', verbose_name=b'Beneficios', blank=True)),
                ('carga_horaria', models.ForeignKey(default=None, blank=True, to='main.CargaHoraria', null=True, verbose_name=b'Jornada Laboral')),
                ('carrera', models.ManyToManyField(default=None, to='main.Carrera', verbose_name=b'carrera', blank=True)),
                ('ciudad', models.ForeignKey(blank=True, to='main.Ciudad', null=True)),
                ('conocimiento', models.ManyToManyField(default=None, to='main.Conocimiento', verbose_name=b'Conocimiento', blank=True)),
                ('empresa', models.ForeignKey(default=None, blank=True, to='empresa.Empresa', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OportunidadCompatibilidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('compatibilidad_academica', models.IntegerField(default=0, null=True, blank=True)),
                ('compatibilidad_cultural', models.IntegerField(default=0, null=True, blank=True)),
                ('compatibilidad_promedio', models.IntegerField(default=0, null=True, blank=True)),
                ('orden', models.IntegerField(null=True, blank=True)),
                ('fecha_creacion', models.DateField(default=None, null=True, blank=True)),
                ('fecha_modificacion', models.DateField(default=None, null=True, blank=True)),
                ('estado', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')])),
                ('estudiante', models.ForeignKey(default=None, blank=True, to='estudiante.Estudiante', null=True)),
                ('oportunidad', models.ForeignKey(default=None, blank=True, to='oportunidad.Oportunidad', null=True)),
            ],
            options={
                'ordering': ['orden'],
            },
        ),
        migrations.CreateModel(
            name='Postulacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado_postulacion', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'P', b'Postulacion'), (b'E', b'En Evaluacion'), (b'F', b'Finalizado')])),
                ('estado_fase', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')])),
                ('usuario_creacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_creacion', models.DateField(default=None, null=True, blank=True)),
                ('usuario_modificacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_modificacion', models.DateField(default=None, null=True, blank=True)),
                ('estado', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')])),
                ('estudiante', models.ForeignKey(default=None, blank=True, to='estudiante.Estudiante', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProcesoFase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('orden', models.IntegerField(default=None, null=True, blank=True)),
                ('mensaje_contenido', models.TextField(default=None, null=True, blank=True)),
                ('mensaje_asunto', models.CharField(default=None, max_length=b'100', null=True, blank=True)),
                ('usuario_creacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_creacion', models.DateField(default=None, null=True, blank=True)),
                ('usuario_modificacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_modificacion', models.DateField(default=None, null=True, blank=True)),
                ('estado', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')])),
            ],
        ),
        migrations.AddField(
            model_name='postulacion',
            name='fase',
            field=models.ForeignKey(default=None, blank=True, to='oportunidad.ProcesoFase', null=True),
        ),
        migrations.AddField(
            model_name='postulacion',
            name='oportunidad',
            field=models.ForeignKey(default=None, blank=True, to='oportunidad.Oportunidad', null=True),
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='fase',
            field=models.ForeignKey(default=None, blank=True, to='oportunidad.ProcesoFase', null=True),
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='grado_estudio',
            field=models.ForeignKey(default=None, blank=True, to='main.GradoEstudio', null=True, verbose_name=b'grado estudios'),
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='graduacion_desde',
            field=models.ForeignKey(related_name='graduacion_desde', default=None, blank=True, to='main.PeriodosGraduacion', null=True),
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='graduacion_hasta',
            field=models.ForeignKey(related_name='graduacion_hasta', default=None, blank=True, to='main.PeriodosGraduacion', null=True),
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='idioma',
            field=models.ManyToManyField(default=None, to='main.Idioma', verbose_name=b'Idioma', blank=True),
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
            name='tipo_carrera',
            field=models.ForeignKey(default=None, blank=True, to='main.TipoCarrera', null=True),
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
            model_name='beneficioextra',
            name='oportunidad',
            field=models.ForeignKey(default=None, blank=True, to='oportunidad.Oportunidad', null=True),
        ),
    ]
