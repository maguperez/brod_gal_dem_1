# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oportunidad', '0023_oportunidad_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='oportunidad',
            name='estado_opotunidad',
            field=models.CharField(default=None, max_length=1, null=True, blank=True, choices=[(b'P', b'Pendiente'), (b'A', b'Abierto'), (b'C', b'Cerrado')]),
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='fecha_modificacion',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='postulacion',
            name='estado',
            field=models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')]),
        ),
        migrations.AddField(
            model_name='postulacion',
            name='fecha_creacion',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='postulacion',
            name='fecha_modificacion',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='oportunidad',
            name='estado',
            field=models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')]),
        ),
    ]
