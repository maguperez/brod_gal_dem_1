# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0004_auto_20151116_1006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='facturacion_anual',
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='numero_funcioarios',
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='sector',
        ),
    ]
