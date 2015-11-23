# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oportunidad', '0008_auto_20151117_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='oportunidad',
            name='estado',
            field=models.CharField(default=None, max_length=1, null=True, blank=True, choices=[(b'Pediente', b'P'), (b'Abierto', b'A'), (b'Cerrado', b'C')]),
        ),
        migrations.AlterField(
            model_name='perfiloportunidad',
            name='grado_estudio',
            field=models.ForeignKey(default=None, blank=True, to='main.GradoEstudio', null=True, verbose_name=b'grado estudioa'),
        ),
    ]
