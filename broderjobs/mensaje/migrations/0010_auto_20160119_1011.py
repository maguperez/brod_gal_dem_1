# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mensaje', '0009_auto_20160118_1125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mensaje',
            name='mensaje_previo',
        ),
        migrations.AddField(
            model_name='mensaje_destinatario',
            name='mensaje_previo',
            field=models.ForeignKey(related_name='respuesta', to='mensaje.Mensaje_Destinatario', null=True),
        ),
    ]
