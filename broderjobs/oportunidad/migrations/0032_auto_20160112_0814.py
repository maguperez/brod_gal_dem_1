# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oportunidad', '0031_auto_20160106_1945'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='oportunidad',
        #     name='estado_opotunidad',
        # ),
        # migrations.AddField(
        #     model_name='oportunidad',
        #     name='estado_oportunidad',
        #     field=models.CharField(default=None, max_length=1, null=True, blank=True, choices=[(b'P', b'Archivado'), (b'A', b'Abierto'), (b'C', b'Cerrado')]),
        # ),
        migrations.AddField(
            model_name='procesofase',
            name='mensaje_asunto',
            field=models.CharField(default=None, max_length=b'100', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='procesofase',
            name='mensaje_contenido',
            field=models.CharField(default=None, max_length=b'1000', null=True, blank=True),
        ),
    ]
