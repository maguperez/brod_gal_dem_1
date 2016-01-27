# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0033_auto_20160127_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividadesextra',
            name='descripcion',
            field=models.TextField(default=None, null=True, blank=True),
        ),
    ]
