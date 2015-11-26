# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_delete_coordenadamap'),
        ('oportunidad', '0017_auto_20151125_1046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oportunidad',
            name='perfil_requerido',
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='carrera',
            field=models.ManyToManyField(default=None, to='main.Carrera', verbose_name=b'carrera', blank=True),
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='conocimiento',
            field=models.ManyToManyField(default=None, to='main.Conocimiento', verbose_name=b'Conocimiento', blank=True),
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='grado_estudio',
            field=models.ForeignKey(default=None, blank=True, to='main.GradoEstudio', null=True, verbose_name=b'grado estudios'),
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='idioma',
            field=models.ManyToManyField(default=None, to='main.Idioma', verbose_name=b'Idioma', blank=True),
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='universidad',
            field=models.ManyToManyField(default=None, to='main.Universidad', verbose_name=b'universidad', blank=True),
        ),
    ]
