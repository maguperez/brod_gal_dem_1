# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_delete_coordenadamap'),
        ('oportunidad', '0018_auto_20151126_1534'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfilrequerido',
            name='carrera',
        ),
        migrations.RemoveField(
            model_name='perfilrequerido',
            name='conocimiento',
        ),
        migrations.RemoveField(
            model_name='perfilrequerido',
            name='grado_estudio',
        ),
        migrations.RemoveField(
            model_name='perfilrequerido',
            name='idioma',
        ),
        migrations.RemoveField(
            model_name='perfilrequerido',
            name='universidad',
        ),
        migrations.RemoveField(
            model_name='oportunidad',
            name='beneficio',
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='beneficio',
            field=models.ManyToManyField(default=None, to='main.Beneficio', verbose_name=b'Beneficios', blank=True),
        ),
        migrations.DeleteModel(
            name='PerfilRequerido',
        ),
    ]
