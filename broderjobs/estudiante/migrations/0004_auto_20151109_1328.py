# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0003_auto_20151109_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='ano_graduacion',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='ano_inicio_estudio',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='carerra',
            field=models.ForeignKey(default=None, blank=True, to='main.Carrera', null=True),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='ciudad',
            field=models.ForeignKey(default=None, blank=True, to='main.Ciudad', null=True),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='grado_estudio',
            field=models.ForeignKey(default=None, blank=True, to='main.GradoEstudio', null=True),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='pais',
            field=models.ForeignKey(default=None, blank=True, to='main.Pais', null=True),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='semestre_graduacion',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='semestre_inicio_estudio',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='universidad',
            field=models.ForeignKey(default=None, blank=True, to='main.Universidad', null=True),
        ),
    ]
