# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0011_auto_20151125_1046'),
        ('oportunidad', '0017_auto_20151125_1046'),
        ('main', '0012_coordenadamap'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CoordenadaMap',
        ),
    ]
