# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oportunidad', '0010_auto_20151124_0904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfiloportunidad',
            name='carrera',
        ),
        migrations.RemoveField(
            model_name='perfiloportunidad',
            name='conocimiento',
        ),
        migrations.RemoveField(
            model_name='perfiloportunidad',
            name='idioma',
        ),
        migrations.RemoveField(
            model_name='perfiloportunidad',
            name='universidad',
        ),
        migrations.AlterField(
            model_name='perfiloportunidad',
            name='grado_estudio',
            field=models.ForeignKey(default=None, blank=True, to='main.GradoEstudio', null=True, verbose_name=b'grado estudios'),
        ),
    ]
