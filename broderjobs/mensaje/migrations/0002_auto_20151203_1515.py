# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mensaje', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensaje',
            name='es_respuesta',
            field=models.IntegerField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='mensaje_destinatario',
            name='fecha_creacion',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='estado',
            field=models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')]),
        ),
        migrations.AlterField(
            model_name='mensaje_destinatario',
            name='estado',
            field=models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')]),
        ),
    ]
