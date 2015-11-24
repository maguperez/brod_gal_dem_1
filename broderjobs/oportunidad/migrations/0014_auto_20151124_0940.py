# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_beneficio_tiporemuneracion'),
        ('oportunidad', '0013_perfilrequerido'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfilrequerido',
            name='carrera',
            field=models.ManyToManyField(default=None, to='main.Carrera', verbose_name=b'carrera', blank=True),
        ),
        migrations.AddField(
            model_name='perfilrequerido',
            name='conocimiento',
            field=models.ManyToManyField(default=None, to='main.Conocimiento', verbose_name=b'Conocimiento', blank=True),
        ),
        migrations.AddField(
            model_name='perfilrequerido',
            name='grado_estudio',
            field=models.ForeignKey(default=None, blank=True, to='main.GradoEstudio', null=True, verbose_name=b'grado estudios'),
        ),
        migrations.AddField(
            model_name='perfilrequerido',
            name='idioma',
            field=models.ManyToManyField(default=None, to='main.Idioma', verbose_name=b'Idioma', blank=True),
        ),
        migrations.AddField(
            model_name='perfilrequerido',
            name='universidad',
            field=models.ManyToManyField(default=None, to='main.Universidad', verbose_name=b'universidad', blank=True),
        ),
    ]
