# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20160401_1528'),
        ('oportunidad', '0002_oportunidad_experiencia'),
    ]

    operations = [
        migrations.AddField(
            model_name='oportunidad',
            name='rama_carrera',
            field=models.ManyToManyField(default=None, to='main.RamaCarrera', verbose_name=b'rama carrera', blank=True),
        ),
    ]
