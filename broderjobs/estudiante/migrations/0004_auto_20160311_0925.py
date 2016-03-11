# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0003_estudiante_semestre_actual'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumen',
            name='descripcion',
            field=models.TextField(default=None, null=True, blank=True),
        ),
    ]
