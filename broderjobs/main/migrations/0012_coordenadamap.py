# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_beneficio_tiporemuneracion'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoordenadaMap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('direccion', models.CharField(max_length=b'50')),
                ('longitud', models.FloatField(default=None, null=True, verbose_name=b'longitud', blank=True)),
                ('latitud', models.FloatField(default=None, null=True, verbose_name=b'longitud', blank=True)),
            ],
        ),
    ]
