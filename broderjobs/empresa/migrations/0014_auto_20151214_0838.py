# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0013_auto_20151214_0517'),
    ]

    operations = [
        migrations.CreateModel(
            name='RankingEmpresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('linea_carrera', models.FloatField(default=None, null=True, blank=True)),
                ('flexibilidad_horarios', models.FloatField(default=None, null=True, blank=True)),
                ('ambiente_trabajo', models.FloatField(default=None, null=True, blank=True)),
                ('salarios', models.FloatField(default=None, null=True, blank=True)),
                ('ranking_general', models.FloatField(default=None, null=True, blank=True)),
                ('fecha_creacion', models.DateField(default=None, null=True, blank=True)),
                ('fecha_modificacion', models.DateField(default=None, null=True, blank=True)),
                ('estado', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')])),
            ],
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='ranking_general',
        ),
        migrations.AddField(
            model_name='rankingempresa',
            name='empresa',
            field=models.ForeignKey(to='empresa.Empresa'),
        ),
    ]
