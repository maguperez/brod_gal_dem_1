# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='fecha_nacimiento',
            field=models.DateField(default=None, null=True, blank=True),
        ),
    ]
