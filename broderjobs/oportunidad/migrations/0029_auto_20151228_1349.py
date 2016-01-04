# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oportunidad', '0028_auto_20151228_1102'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='oportunidad',
        #     name='estado_opotunidad',
        # ),
        # migrations.AddField(
        #     model_name='oportunidad',
        #     name='estado_oportunidad',
        #     field=models.CharField(default=None, max_length=1, null=True, blank=True, choices=[(b'P', b'Pendiente'), (b'A', b'Abierto'), (b'C', b'Cerrado')]),
        # ),
        migrations.AddField(
            model_name='oportunidad',
            name='fase',
            field=models.ForeignKey(default=None, blank=True, to='oportunidad.ProcesoFase', null=True),
        ),
        migrations.AddField(
            model_name='postulacion',
            name='fase',
            field=models.ForeignKey(default=None, blank=True, to='oportunidad.ProcesoFase', null=True),
        ),
    ]
