# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cultura_empresarial', '0004_empresarespuestas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresacultura',
            name='porcentaje_adhocracia',
            field=models.FloatField(default=None, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='empresacultura',
            name='porcentaje_clan',
            field=models.FloatField(default=None, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='empresacultura',
            name='porcentaje_jerarquico',
            field=models.FloatField(default=None, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='empresacultura',
            name='porcentaje_racional',
            field=models.FloatField(default=None, null=True, blank=True),
        ),
    ]
