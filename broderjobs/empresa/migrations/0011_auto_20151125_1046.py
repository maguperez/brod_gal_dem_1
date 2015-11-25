# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0010_empresa_coordenadas_map'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='coordenadas_map',
        ),
        migrations.AddField(
            model_name='empresa',
            name='direccion_map',
            field=models.CharField(default=None, max_length=b'100', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='empresa',
            name='latitud',
            field=models.FloatField(default=None, null=True, verbose_name=b'latitud', blank=True),
        ),
        migrations.AddField(
            model_name='empresa',
            name='longitud',
            field=models.FloatField(default=None, null=True, verbose_name=b'longitud', blank=True),
        ),
    ]
