# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oportunidad', '0021_auto_20151130_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='oportunidad',
            name='fecha_creacion',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='fecha_publicacion',
            field=models.DateField(default=None, null=True, blank=True),
        ),
    ]
