# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('mensaje', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='fecha_modificacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='mensaje_destinatario',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='mensaje_destinatario',
            name='fecha_modificacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='notificacion',
            name='fecha_envio',
            field=models.DateTimeField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='notificacion',
            name='fecha_modificacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
    ]
