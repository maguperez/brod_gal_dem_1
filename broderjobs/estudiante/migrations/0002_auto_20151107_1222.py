# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiante',
            name='carga_horaria',
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='ciudad',
        ),
        migrations.AddField(
            model_name='estudiante',
            name='ano_graduacion',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='ano_inicio_estudio',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='semestre_graduacion',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='semestre_inicio_estudio',
            field=models.IntegerField(default=0),
        ),
    ]
