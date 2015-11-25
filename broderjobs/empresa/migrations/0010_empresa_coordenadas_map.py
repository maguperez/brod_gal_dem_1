# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_coordenadamap'),
        ('empresa', '0009_auto_20151118_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='coordenadas_map',
            field=models.ForeignKey(blank=True, to='main.CoordenadaMap', null=True),
        ),
    ]
