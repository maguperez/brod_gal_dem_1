# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cultura_empresarial', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preguntacultura',
            name='descripcion',
            field=models.TextField(default=None, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='respuestacultura',
            name='descripcion',
            field=models.TextField(default=None, null=True, blank=True),
        ),
    ]
