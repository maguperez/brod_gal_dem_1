# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='remuneracion_max',
            field=models.CharField(default=None, max_length=b'50', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='remuneracion_min',
            field=models.CharField(default=None, max_length=b'50', null=True, blank=True),
        ),
    ]
