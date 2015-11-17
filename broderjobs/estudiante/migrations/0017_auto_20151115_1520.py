# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_conocimiento'),
        ('estudiante', '0016_auto_20151115_1435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudianteidioma',
            name='estudiante',
        ),
        migrations.RemoveField(
            model_name='estudianteidioma',
            name='idioma',
        ),
        migrations.AddField(
            model_name='estudiante',
            name='idioma',
            field=models.ManyToManyField(default=None, to='main.Idioma', verbose_name=b'Idioma', blank=True),
        ),
        migrations.DeleteModel(
            name='EstudianteIdioma',
        ),
    ]
