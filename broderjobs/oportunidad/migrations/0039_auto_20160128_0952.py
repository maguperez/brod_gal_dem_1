# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oportunidad', '0038_auto_20160127_1832'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='oportunidad',
        #     name='estado_opotunidad',
        # ),
        migrations.RemoveField(
            model_name='oportunidad',
            name='graduacion_desde',
        ),
        migrations.RemoveField(
            model_name='oportunidad',
            name='graduacion_hasta',
        ),
        # migrations.AddField(
        #     model_name='oportunidad',
        #     name='estado_oportunidad',
        #     field=models.CharField(default=None, max_length=1, null=True, blank=True, choices=[(b'P', b'Archivado'), (b'A', b'Abierto'), (b'C', b'Cerrado')]),
        # ),
    ]
