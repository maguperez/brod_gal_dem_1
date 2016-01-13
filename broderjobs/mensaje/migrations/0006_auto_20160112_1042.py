# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mensaje', '0005_notificacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensaje',
            name='usuario_creacion',
            field=models.CharField(default=None, max_length=b'50', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='mensaje_destinatario',
            name='usuario_creacion',
            field=models.CharField(default=None, max_length=b'50', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='notificacion',
            name='leido',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='notificacion',
            name='usuario_creacion',
            field=models.CharField(default=None, max_length=b'50', null=True, blank=True),
        ),
    ]
