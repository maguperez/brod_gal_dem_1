# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0027_auto_20151222_0950'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='carrera_referencial',
            field=models.CharField(default=None, max_length=b'100', null=True, blank=True),
        ),
    ]
