# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0012_auto_20151113_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='ano_graduacion',
            field=models.CharField(default=None, max_length=4, null=True, blank=True, choices=[(1980, 2020), (1980, 2020)]),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='ano_inicio_estudio',
            field=models.CharField(default=None, max_length=4, null=True, blank=True, choices=[(1980, 2020), (1980, 2020)]),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='semestre_graduacion',
            field=models.CharField(default=0, max_length=2, blank=True, choices=[(1, 1), (2, 2)]),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='semestre_inicio_estudio',
            field=models.CharField(default=None, max_length=2, null=True, blank=True, choices=[(1, 1), (2, 2)]),
        ),
    ]
