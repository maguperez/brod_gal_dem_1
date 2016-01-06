# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oportunidad', '0029_auto_20151228_1349'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='oportunidad',
        #     name='estado_opotunidad',
        # ),
        migrations.RemoveField(
            model_name='oportunidad',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='procesofase',
            name='usuario',
        ),
        # migrations.AddField(
        #     model_name='oportunidad',
        #     name='estado_oportunidad',
        #     field=models.CharField(default=None, max_length=1, null=True, blank=True, choices=[(b'P', b'Archivado'), (b'A', b'Abierto'), (b'C', b'Cerrado')]),
        # ),
        migrations.AddField(
            model_name='oportunidad',
            name='usuario_creacion',
            field=models.CharField(default=None, max_length=b'50', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='usuario_modificacion',
            field=models.CharField(default=None, max_length=b'50', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='postulacion',
            name='usuario_creacion',
            field=models.CharField(default=None, max_length=b'50', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='postulacion',
            name='usuario_modificacion',
            field=models.CharField(default=None, max_length=b'50', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='procesofase',
            name='usuario_creacion',
            field=models.CharField(default=None, max_length=b'50', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='procesofase',
            name='usuario_modificacion',
            field=models.CharField(default=None, max_length=b'50', null=True, blank=True),
        ),
    ]
