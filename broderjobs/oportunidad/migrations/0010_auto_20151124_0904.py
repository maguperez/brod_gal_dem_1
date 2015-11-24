# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oportunidad', '0009_auto_20151123_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfiloportunidad',
            name='perfil',
            field=models.CharField(default=None, max_length=b'10', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='oportunidad',
            name='estado',
            field=models.CharField(default=None, max_length=1, null=True, blank=True, choices=[(b'P', b'Pendiente'), (b'A', b'Abierto'), (b'C', b'Cerrado')]),
        ),
    ]
