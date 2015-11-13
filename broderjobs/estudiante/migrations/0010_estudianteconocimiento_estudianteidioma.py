# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_conocimiento'),
        ('estudiante', '0009_auto_20151112_1017'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstudianteConocimiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('conocimiento', models.ForeignKey(to='main.Conocimiento')),
                ('estudiante', models.ForeignKey(to='estudiante.Estudiante')),
            ],
        ),
        migrations.CreateModel(
            name='EstudianteIdioma',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estudiante', models.ForeignKey(to='estudiante.Estudiante')),
                ('idioma', models.ForeignKey(to='main.Idioma')),
            ],
        ),
    ]
