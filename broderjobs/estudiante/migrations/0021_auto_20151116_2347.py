# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0020_auto_20151116_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voluntariado',
            name='estudiante',
            field=models.ForeignKey(default=None, blank=True, to='estudiante.Estudiante', null=True),
        ),
    ]
