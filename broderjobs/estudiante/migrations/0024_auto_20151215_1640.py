# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0023_auto_20151215_1638'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experienciaprofesional',
            old_name='empresa_referancial',
            new_name='empresa_referencial',
        ),
    ]
