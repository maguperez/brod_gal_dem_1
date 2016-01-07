# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mensaje', '0003_auto_20160107_0900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mensaje',
            name='postulacion',
        ),
        migrations.AddField(
            model_name='mensaje',
            name='oportunidad',
            field=models.ForeignKey(default=None, blank=True, to='oportunidad.Oportunidad', null=True),
        ),
    ]
