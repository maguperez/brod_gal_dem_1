# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20160309_0901'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='enviar_correo',
            field=models.BooleanField(default=False),
        ),
    ]
