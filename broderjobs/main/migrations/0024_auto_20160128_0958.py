# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20160128_0954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='periodosgraduacion',
            name='secuencia_tecnica',
        ),
        migrations.RemoveField(
            model_name='periodosgraduacion',
            name='secuencia_universitaria',
        ),
    ]
