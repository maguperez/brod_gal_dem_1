# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20151203_1517'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeriodoGraduacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_creacion', models.DateField(default=None, null=True, blank=True)),
                ('fecha_modificacion', models.DateField(default=None, null=True, blank=True)),
                ('estado', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')])),
            ],
        ),
        migrations.AlterField(
            model_name='beneficio',
            name='descripcion',
            field=models.CharField(default=None, max_length=b'50', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cargahoraria',
            name='descripcion',
            field=models.CharField(default=None, max_length=b'50', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='carrera',
            name='descripcion',
            field=models.CharField(default=None, max_length=b'50', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='conocimiento',
            name='descripcion',
            field=models.CharField(default=None, max_length=b'50', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='idioma',
            name='descripcion',
            field=models.CharField(default=None, max_length=b'50', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tipopuesto',
            name='descripcion',
            field=models.CharField(default=None, max_length=b'50', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tiporemuneracion',
            name='descripcion',
            field=models.CharField(default=None, max_length=b'50', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='universidad',
            name='descripcion',
            field=models.CharField(default=None, max_length=b'50', null=True, blank=True),
        ),
    ]
