# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0025_videourl'),
        ('estudiante', '0035_auto_20160217_1118'),
        ('cultura_empresarial', '0005_auto_20160212_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstudianteCultura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('porcentaje_clan', models.FloatField(default=None, null=True, blank=True)),
                ('porcentaje_adhocracia', models.FloatField(default=None, null=True, blank=True)),
                ('porcentaje_jerarquico', models.FloatField(default=None, null=True, blank=True)),
                ('porcentaje_racional', models.FloatField(default=None, null=True, blank=True)),
                ('orden', models.IntegerField(default=None, null=True, blank=True)),
                ('usuario_creacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_creacion', models.DateField(default=None, null=True, blank=True)),
                ('usuario_modificacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_modificacion', models.DateField(default=None, null=True, blank=True)),
                ('estado', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')])),
                ('estudiante', models.ForeignKey(default=None, blank=True, to='estudiante.Estudiante', null=True)),
            ],
            options={
                'ordering': ['estudiante'],
            },
        ),
        migrations.CreateModel(
            name='EstudianteEmpresaCultura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('porcentaje_clan', models.FloatField(default=None, null=True, blank=True)),
                ('porcentaje_adhocracia', models.FloatField(default=None, null=True, blank=True)),
                ('porcentaje_jerarquico', models.FloatField(default=None, null=True, blank=True)),
                ('porcentaje_racional', models.FloatField(default=None, null=True, blank=True)),
                ('compatibilidad_cultural', models.FloatField(default=None, null=True, blank=True)),
                ('orden', models.IntegerField(default=None, null=True, blank=True)),
                ('usuario_creacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_creacion', models.DateField(default=None, null=True, blank=True)),
                ('usuario_modificacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_modificacion', models.DateField(default=None, null=True, blank=True)),
                ('estado', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')])),
                ('empresa', models.ForeignKey(default=None, blank=True, to='empresa.Empresa', null=True)),
                ('estudiante', models.ForeignKey(default=None, blank=True, to='estudiante.Estudiante', null=True)),
            ],
            options={
                'ordering': ['estudiante', 'empresa'],
            },
        ),
    ]
