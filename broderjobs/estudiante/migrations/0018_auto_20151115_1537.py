# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_conocimiento'),
        ('estudiante', '0017_auto_20151115_1520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudianteconocimiento',
            name='conocimiento',
        ),
        migrations.RemoveField(
            model_name='estudianteconocimiento',
            name='estudiante',
        ),
        migrations.AddField(
            model_name='estudiante',
            name='conocimiento',
            field=models.ManyToManyField(default=None, to='main.Conocimiento', verbose_name=b'Conocimiento', blank=True),
        ),
        migrations.DeleteModel(
            name='EstudianteConocimiento',
        ),
    ]
