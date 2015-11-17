# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oportunidad', '0003_auto_20151116_1428'),
    ]

    operations = [
        migrations.RenameField(
            model_name='oportunidad',
            old_name='carga',
            new_name='carga_horaria',
        ),
    ]
