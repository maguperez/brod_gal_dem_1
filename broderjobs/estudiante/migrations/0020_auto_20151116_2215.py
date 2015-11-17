# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0019_auto_20151115_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='carga_horaria',
            field=models.ForeignKey(default=None, blank=True, to='main.CargaHoraria', null=True),
        ),
        migrations.AlterField(
            model_name='experienciaprofesional',
            name='estudiante',
            field=models.ForeignKey(default=None, blank=True, to='estudiante.Estudiante', null=True),
        ),
        migrations.AlterField(
            model_name='experienciaprofesional',
            name='puesto',
            field=models.ForeignKey(default=None, blank=True, to='empresa.Puesto', null=True),
        ),
    ]
