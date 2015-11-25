# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oportunidad', '0016_oportunidad_coordenadas_map'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oportunidad',
            name='coordenadas_map',
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='direccion_map',
            field=models.CharField(default=None, max_length=b'100', null=True, blank=True),
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
    ]
