# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_carrera_universidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciudad',
            name='pais',
            field=models.ForeignKey(to='main.Pais'),
        ),
    ]
