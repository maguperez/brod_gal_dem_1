# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oportunidad', '0040_auto_20160128_1004'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='oportunidad',
        #     name='estado_opotunidad',
        # ),
        migrations.AddField(
            model_name='oportunidad',
            name='edad_desde',
            field=models.IntegerField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='edad_hasta',
            field=models.IntegerField(default=None, null=True, blank=True),
        ),
        # migrations.AddField(
        #     model_name='oportunidad',
        #     name='estado_oportunidad',
        #     field=models.CharField(default=None, max_length=1, null=True, blank=True, choices=[(b'P', b'Archivado'), (b'A', b'Abierto'), (b'C', b'Cerrado')]),
        # ),
        migrations.AddField(
            model_name='oportunidad',
            name='genero',
            field=models.CharField(default=b'', max_length=1, null=True, blank=True, choices=[(b'M', b'Masculino'), (b'F', b'Femenino')]),
        ),
    ]
