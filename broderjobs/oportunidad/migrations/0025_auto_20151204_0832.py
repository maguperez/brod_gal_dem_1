# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oportunidad', '0024_auto_20151203_1514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postulacion',
            name='fecha',
        ),
        migrations.AddField(
            model_name='postulacion',
            name='estado_postulacion',
            field=models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'P', b'Postulacion'), (b'E', b'En Evaluacion'), (b'F', b'Finalizado')]),
        ),
    ]
