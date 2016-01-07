# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mensaje', '0002_auto_20151203_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='contenido',
            field=models.TextField(default=None, null=True, blank=True),
        ),
    ]
