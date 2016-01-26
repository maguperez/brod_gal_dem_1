# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_persona_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficio',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='beneficio',
            name='fecha_modificacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cargahoraria',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cargahoraria',
            name='fecha_modificacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='carrera',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='carrera',
            name='fecha_modificacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ciudad',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ciudad',
            name='fecha_modificacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='conocimiento',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='conocimiento',
            name='fecha_modificacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='gradoestudio',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='gradoestudio',
            name='fecha_modificacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='idioma',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='idioma',
            name='fecha_modificacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='pais',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='pais',
            name='fecha_modificacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='periodosgraduacion',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='periodosgraduacion',
            name='fecha_modificacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='fecha_modificacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tipocarrera',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tipocarrera',
            name='fecha_modificacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tipopuesto',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tipopuesto',
            name='fecha_modificacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tiporemuneracion',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tiporemuneracion',
            name='fecha_modificacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='universidad',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='universidad',
            name='fecha_modificacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
    ]
