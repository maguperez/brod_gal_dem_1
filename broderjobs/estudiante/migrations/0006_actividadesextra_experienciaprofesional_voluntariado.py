# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0001_initial'),
        ('estudiante', '0005_auto_20151109_1505'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActividadesExtra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=b'50')),
                ('organizacion', models.CharField(max_length=b'50')),
                ('Estudiante', models.ForeignKey(to='estudiante.Estudiante')),
            ],
        ),
        migrations.CreateModel(
            name='ExperienciaProfesional',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_desde', models.DateField(null=True)),
                ('fecha_hasta', models.DateField(default=None, null=True, blank=True)),
                ('trabajo_actual', models.CharField(default=b'N', max_length=1)),
                ('descripcion', models.CharField(default=None, max_length=b'100', null=True)),
                ('Estudiante', models.ForeignKey(to='estudiante.Estudiante')),
                ('empresa', models.ForeignKey(default=None, blank=True, to='empresa.Empresa', null=True)),
                ('puesto', models.ForeignKey(to='empresa.Puesto')),
            ],
        ),
        migrations.CreateModel(
            name='Voluntariado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cargo', models.CharField(max_length=b'50')),
                ('organizacion', models.CharField(max_length=b'50')),
                ('fecha_desde', models.DateField(null=True)),
                ('fecha_hasta', models.DateField(default=None, null=True, blank=True)),
                ('voluntariado_actual', models.CharField(default=b'N', max_length=1)),
                ('descripcion', models.CharField(default=None, max_length=b'100', null=True)),
                ('Estudiante', models.ForeignKey(to='estudiante.Estudiante')),
            ],
        ),
    ]
