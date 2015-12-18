# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0024_auto_20151215_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='experienciaprofesional',
            name='puesto_referencial',
            field=models.CharField(default=None, max_length=b'50', null=True),
        ),
    ]
