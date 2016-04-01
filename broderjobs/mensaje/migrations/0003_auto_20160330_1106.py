# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mensaje', '0002_auto_20160330_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificacion',
            name='fecha_envio',
            field=models.DateTimeField(default=None, null=True, blank=True),
        ),
    ]
