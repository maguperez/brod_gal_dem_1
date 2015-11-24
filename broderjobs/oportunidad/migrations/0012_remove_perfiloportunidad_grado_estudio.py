# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oportunidad', '0011_auto_20151124_0928'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfiloportunidad',
            name='grado_estudio',
        ),
    ]
