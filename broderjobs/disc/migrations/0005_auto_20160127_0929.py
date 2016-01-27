# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0033_auto_20160127_0929'),
        ('disc', '0004_auto_20160127_0846'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscCodificacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('letra', models.CharField(default=b'', max_length=1, null=True, blank=True, choices=[(b'D', b'D'), (b'I', b'I'), (b'S', b'S'), (b'C', b'C')])),
                ('segmento', models.IntegerField(default=None, null=True, blank=True)),
                ('orden', models.IntegerField(default=None, null=True, blank=True)),
                ('usuario_creacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_creacion', models.DateField(default=datetime.datetime.now, null=True, blank=True)),
                ('usuario_modificacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_modificacion', models.DateField(default=datetime.datetime.now, null=True, blank=True)),
                ('estado', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')])),
            ],
            options={
                'ordering': ['letra', 'orden'],
            },
        ),
        migrations.CreateModel(
            name='EstudiantePatron',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('orden', models.IntegerField(default=None, null=True, blank=True)),
                ('usuario_creacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_creacion', models.DateField(default=datetime.datetime.now, null=True, blank=True)),
                ('usuario_modificacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_modificacion', models.DateField(default=datetime.datetime.now, null=True, blank=True)),
                ('estado', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')])),
                ('estudiante', models.ForeignKey(default=None, blank=True, to='estudiante.Estudiante', null=True)),
                ('patron_perfil', models.ForeignKey(default=None, blank=True, to='disc.PatronPerfil', null=True)),
            ],
            options={
                'ordering': ['estudiante'],
            },
        ),
        migrations.CreateModel(
            name='EstudianteRespuestas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(default=None, max_length=b'200', null=True, blank=True)),
                ('letra_mas', models.CharField(default=b'', max_length=1, null=True, blank=True, choices=[(b'D', b'D'), (b'I', b'I'), (b'S', b'S'), (b'C', b'C')])),
                ('letra_menos', models.CharField(default=b'', max_length=1, null=True, blank=True, choices=[(b'D', b'D'), (b'I', b'I'), (b'S', b'S'), (b'C', b'C')])),
                ('orden', models.IntegerField(default=None, null=True, blank=True)),
                ('usuario_creacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_creacion', models.DateField(default=datetime.datetime.now, null=True, blank=True)),
                ('usuario_modificacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_modificacion', models.DateField(default=datetime.datetime.now, null=True, blank=True)),
                ('estado', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')])),
                ('estudiante', models.ForeignKey(default=None, blank=True, to='estudiante.Estudiante', null=True)),
                ('pregunta', models.ForeignKey(default=None, blank=True, to='disc.Pregunta', null=True)),
            ],
            options={
                'ordering': ['estudiante', 'pregunta', 'orden'],
            },
        ),
        migrations.RemoveField(
            model_name='respuestaestudiante',
            name='estudiante',
        ),
        migrations.RemoveField(
            model_name='respuestaestudiante',
            name='pregunta',
        ),
        migrations.DeleteModel(
            name='RespuestaEstudiante',
        ),
    ]
