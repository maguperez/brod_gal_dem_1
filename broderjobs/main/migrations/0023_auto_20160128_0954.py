# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20160126_1127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='periodosgraduacion',
            old_name='valor',
            new_name='secuencia_tecnica',
        ),
        migrations.AddField(
            model_name='periodosgraduacion',
            name='secuencia_universitaria',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
