# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mensaje', '0008_notificacion_postulacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mensaje',
            name='es_respuesta',
        ),
        migrations.AddField(
            model_name='mensaje',
            name='mensaje_previo',
            field=models.ForeignKey(related_name='respuesta', to='mensaje.Mensaje', null=True),
        ),
    ]
