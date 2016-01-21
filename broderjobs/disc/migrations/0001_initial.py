# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0030_auto_20160120_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('orden', models.IntegerField(default=None, null=True, blank=True)),
                ('usuario_creacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_creacion', models.DateField(default=None, null=True, blank=True)),
                ('usuario_modificacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_modificacion', models.DateField(default=None, null=True, blank=True)),
                ('estado', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')])),
            ],
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('letra', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'D', b'D'), (b'I', b'I'), (b'S', b'S'), (b'C', b'C')])),
                ('orden', models.IntegerField(default=None, null=True, blank=True)),
                ('usuario_creacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_creacion', models.DateField(default=None, null=True, blank=True)),
                ('usuario_modificacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_modificacion', models.DateField(default=None, null=True, blank=True)),
                ('estado', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')])),
                ('pregunta', models.ForeignKey(default=None, blank=True, to='disc.Pregunta', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RespuestaEstudiante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('letra_mas', models.CharField(default=b'', max_length=1, null=True, blank=True, choices=[(b'D', b'D'), (b'I', b'I'), (b'S', b'S'), (b'C', b'C')])),
                ('letra_menos', models.CharField(default=b'', max_length=1, null=True, blank=True, choices=[(b'D', b'D'), (b'I', b'I'), (b'S', b'S'), (b'C', b'C')])),
                ('orden', models.IntegerField(default=None, null=True, blank=True)),
                ('usuario_creacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_creacion', models.DateField(default=None, null=True, blank=True)),
                ('usuario_modificacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_modificacion', models.DateField(default=None, null=True, blank=True)),
                ('estado', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')])),
                ('estudiante', models.ForeignKey(default=None, blank=True, to='estudiante.Estudiante', null=True)),
                ('respuesta', models.ForeignKey(default=None, blank=True, to='disc.Respuesta', null=True)),
            ],
        ),
    ]
