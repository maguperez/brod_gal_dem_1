# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20160115_1024'),
        ('oportunidad', '0033_auto_20160112_0817'),
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
        migrations.RemoveField(
            model_name='oportunidad',
            name='grado_estudio',
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='grado_estudio',
            field=models.ManyToManyField(default=None, to='main.GradoEstudio', null=True, verbose_name=b'grado estudios', blank=True),
        ),
        migrations.AlterField(
            model_name='oportunidad',
            name='graduacion_desde',
            field=models.CharField(default=None, max_length=10, null=True, blank=True, choices=[(b'1', '5 a\xf1o para graduarse'), (b'2', '4 a\xf1os para graduarse'), (b'3', '3 a\xf1os para graduarse'), (b'4', '2 a\xf1os para graduarse '), (b'5', '1 a\xf1o para graduarse'), (b'6', '1 a\xf1o de graduado'), (b'7', '2 a\xf1os de graduado')]),
        ),
        migrations.AlterField(
            model_name='oportunidad',
            name='graduacion_hasta',
            field=models.CharField(default=None, max_length=10, null=True, blank=True, choices=[(b'1', '5 a\xf1o para graduarse'), (b'2', '4 a\xf1os para graduarse'), (b'3', '3 a\xf1os para graduarse'), (b'4', '2 a\xf1os para graduarse '), (b'5', '1 a\xf1o para graduarse'), (b'6', '1 a\xf1o de graduado'), (b'7', '2 a\xf1os de graduado')]),
        ),
    ]
