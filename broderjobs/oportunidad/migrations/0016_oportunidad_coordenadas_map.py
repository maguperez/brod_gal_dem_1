# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_coordenadamap'),
        ('oportunidad', '0015_auto_20151124_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='oportunidad',
            name='coordenadas_map',
            field=models.ForeignKey(blank=True, to='main.CoordenadaMap', null=True),
        ),
    ]
