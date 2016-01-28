# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_auto_20160128_0958'),
        ('oportunidad', '0039_auto_20160128_0952'),
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
            model_name='oportunidad',
            name='graduacion_desde',
            field=models.ForeignKey(related_name='graduacion_desde', default=None, blank=True, to='main.PeriodosGraduacion', null=True),
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='graduacion_hasta',
            field=models.ForeignKey(related_name='graduacion_hasta', default=None, blank=True, to='main.PeriodosGraduacion', null=True),
        ),
    ]
