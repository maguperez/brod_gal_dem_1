# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('empresa', '0012_auto_20151203_1517'),
    ]

    operations = [
        migrations.CreateModel(
            name='EvaluacionEmpresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('linea_carrera', models.FloatField(default=None, null=True, blank=True)),
                ('flexibilidad_horarios', models.FloatField(default=None, null=True, blank=True)),
                ('ambiente_trabajo', models.FloatField(default=None, null=True, blank=True)),
                ('salarios', models.FloatField(default=None, null=True, blank=True)),
                ('ranking', models.FloatField(default=None, null=True, blank=True)),
                ('fecha_creacion', models.DateField(default=None, null=True, blank=True)),
                ('fecha_modificacion', models.DateField(default=None, null=True, blank=True)),
                ('estado', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')])),
            ],
        ),
        migrations.AlterField(
            model_name='empresa',
            name='ranking_general',
            field=models.FloatField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='evaluacionempresa',
            name='empresa',
            field=models.ForeignKey(to='empresa.Empresa'),
        ),
        migrations.AddField(
            model_name='evaluacionempresa',
            name='usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
