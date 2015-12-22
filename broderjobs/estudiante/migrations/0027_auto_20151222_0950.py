# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0026_auto_20151221_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='experienciaprofesional',
            name='empresa_referencial',
            field=models.CharField(default=None, max_length=b'50', null=True),
        ),
        migrations.AddField(
            model_name='experienciaprofesional',
            name='puesto_referencial',
            field=models.CharField(default=None, max_length=b'50', null=True),
        ),
    ]
