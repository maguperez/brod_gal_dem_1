# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20151101_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='telefono',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='persona',
            name='tipo_persona',
            field=models.CharField(default=b'E', max_length=1),
        ),
    ]
