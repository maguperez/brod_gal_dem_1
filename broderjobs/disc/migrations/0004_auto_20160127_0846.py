# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disc', '0003_auto_20160127_0806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='respuestaestudiante',
            name='respuesta',
        ),
        migrations.AddField(
            model_name='respuestaestudiante',
            name='pregunta',
            field=models.ForeignKey(default=None, blank=True, to='disc.Pregunta', null=True),
        ),
    ]
