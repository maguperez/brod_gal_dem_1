# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oportunidad', '0027_auto_20151208_1710'),
    ]

    operations = [
        migrations.RenameField(
            model_name='oportunidad',
            old_name='estado_opotunidad',
            new_name='estado_oportunidad',
        ),
    ]
