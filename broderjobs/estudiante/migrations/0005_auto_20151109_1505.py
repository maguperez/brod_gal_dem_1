# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0004_auto_20151109_1328'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estudiante',
            old_name='carerra',
            new_name='carrera',
        ),
    ]
