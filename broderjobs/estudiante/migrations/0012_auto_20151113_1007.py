# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0011_estudiante_tipo_puesto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='tipo_puesto',
            field=models.ManyToManyField(default=None, to='main.TipoPuesto', verbose_name=b'Tipo Puesto', blank=True),
        ),
    ]
