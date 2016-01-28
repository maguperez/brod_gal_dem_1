# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disc', '0009_auto_20160127_1700'),
    ]

    operations = [
        migrations.RenameField(
            model_name='disccodificacion',
            old_name='valor',
            new_name='valor_desde',
        ),
        migrations.AddField(
            model_name='disccodificacion',
            name='valor_hasta',
            field=models.IntegerField(default=None, null=True, blank=True),
        ),
    ]
