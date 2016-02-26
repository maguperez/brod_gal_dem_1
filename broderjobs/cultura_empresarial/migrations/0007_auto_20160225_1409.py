# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cultura_empresarial', '0006_estudiantecultura_estudianteempresacultura'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudianteempresacultura',
            name='compatibilidad_cultural',
            field=models.FloatField(default=0.0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='estudianteempresacultura',
            name='porcentaje_adhocracia',
            field=models.FloatField(default=0.0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='estudianteempresacultura',
            name='porcentaje_clan',
            field=models.FloatField(default=0.0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='estudianteempresacultura',
            name='porcentaje_jerarquico',
            field=models.FloatField(default=0.0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='estudianteempresacultura',
            name='porcentaje_racional',
            field=models.FloatField(default=0.0, null=True, blank=True),
        ),
    ]
