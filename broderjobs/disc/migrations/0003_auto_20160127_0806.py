# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('disc', '0002_auto_20160122_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patronperfil',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='patronperfil',
            name='fecha_modificacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='fecha_modificacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='respuestaestudiante',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='respuestaestudiante',
            name='fecha_modificacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
    ]
