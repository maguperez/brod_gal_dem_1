# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0028_estudiante_carrera_referencial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividadesextra',
            name='descripcion',
            field=models.CharField(default=None, max_length=b'1000', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='experienciaprofesional',
            name='descripcion',
            field=models.CharField(default=None, max_length=b'1000', null=True),
        ),
        migrations.AlterField(
            model_name='voluntariado',
            name='descripcion',
            field=models.CharField(default=None, max_length=b'1000', null=True, blank=True),
        ),
    ]
