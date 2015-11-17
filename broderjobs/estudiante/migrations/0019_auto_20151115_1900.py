# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0018_auto_20151115_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experienciaprofesional',
            name='fecha_desde',
            field=models.DateField(default=None, null=True, blank=True),
        ),
    ]
