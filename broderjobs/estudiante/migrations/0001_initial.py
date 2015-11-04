# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_carrera_universidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('carga_horaria', models.CharField(max_length=1, null=True)),
                ('carerra', models.OneToOneField(default=0, to='main.Carrera')),
                ('ciudad', models.OneToOneField(default=0, to='main.Ciudad')),
                ('grado_estudio', models.OneToOneField(default=0, to='main.GradoEstudio')),
                ('pais', models.OneToOneField(default=0, to='main.Pais')),
                ('persona', models.OneToOneField(to='main.Persona')),
                ('universidad', models.OneToOneField(default=0, to='main.Universidad')),
            ],
        ),
    ]
