# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mensaje', '0006_auto_20160112_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensaje_destinatario',
            name='fecha_envio',
            field=models.DateTimeField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='notificacion',
            name='fecha_envio',
            field=models.DateTimeField(default=None, null=True, blank=True),
        ),
    ]
