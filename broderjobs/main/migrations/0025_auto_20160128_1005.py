# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_auto_20160128_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='periodosgraduacion',
            name='secuencia_tecnica',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='periodosgraduacion',
            name='secuencia_universitaria',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
