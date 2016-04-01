# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0006_auto_20160331_1523'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estudiante',
            old_name='remuneracion_max',
            new_name='remuneracion',
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='remuneracion_min',
        ),
    ]
