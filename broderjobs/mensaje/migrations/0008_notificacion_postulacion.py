# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        # ('oportunidad', '0034_auto_20160113_0845'),
        ('mensaje', '0007_auto_20160112_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificacion',
            name='postulacion',
            field=models.ForeignKey(default=None, blank=True, to='oportunidad.Postulacion', null=True),
        ),
    ]
