# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0025_videourl'),
    ]

    operations = [
        migrations.CreateModel(
            name='CulturaMatrizDISC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('letra_d', models.IntegerField(default=None, null=True, blank=True)),
                ('letra_i', models.IntegerField(default=None, null=True, blank=True)),
                ('letra_s', models.IntegerField(default=None, null=True, blank=True)),
                ('letra_c', models.IntegerField(default=None, null=True, blank=True)),
                ('resultado', models.IntegerField(default=None, null=True, blank=True)),
                ('orden', models.IntegerField(default=None, null=True, blank=True)),
                ('usuario_creacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_creacion', models.DateField(default=None, null=True, blank=True)),
                ('usuario_modificacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_modificacion', models.DateField(default=None, null=True, blank=True)),
                ('estado', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')])),
            ],
            options={
                'ordering': ['perfil_cultura'],
            },
        ),
        migrations.CreateModel(
            name='EmpresaCultura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('porcentaje_clan', models.IntegerField(default=None, null=True, blank=True)),
                ('porcentaje_adhocracia', models.IntegerField(default=None, null=True, blank=True)),
                ('porcentaje_jerarquico', models.IntegerField(default=None, null=True, blank=True)),
                ('porcentaje_racional', models.IntegerField(default=None, null=True, blank=True)),
                ('orden', models.IntegerField(default=None, null=True, blank=True)),
                ('usuario_creacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_creacion', models.DateField(default=None, null=True, blank=True)),
                ('usuario_modificacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_modificacion', models.DateField(default=None, null=True, blank=True)),
                ('estado', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')])),
                ('empresa', models.ForeignKey(default=None, blank=True, to='empresa.Empresa', null=True)),
            ],
            options={
                'ordering': ['empresa'],
            },
        ),
        migrations.CreateModel(
            name='Perfil_Cultura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('descripcion', models.TextField(default=None, null=True, blank=True)),
                ('orden', models.IntegerField(default=None, null=True, blank=True)),
                ('usuario_creacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_creacion', models.DateField(default=None, null=True, blank=True)),
                ('usuario_modificacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_modificacion', models.DateField(default=None, null=True, blank=True)),
                ('estado', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')])),
            ],
            options={
                'ordering': ['orden'],
            },
        ),
        migrations.CreateModel(
            name='PreguntaCultura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('orden', models.IntegerField(default=None, null=True, blank=True)),
                ('usuario_creacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_creacion', models.DateField(default=None, null=True, blank=True)),
                ('usuario_modificacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_modificacion', models.DateField(default=None, null=True, blank=True)),
                ('estado', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')])),
            ],
            options={
                'ordering': ['orden'],
            },
        ),
        migrations.CreateModel(
            name='RespuestaCultura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('orden', models.IntegerField(default=None, null=True, blank=True)),
                ('usuario_creacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_creacion', models.DateField(default=None, null=True, blank=True)),
                ('usuario_modificacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_modificacion', models.DateField(default=None, null=True, blank=True)),
                ('estado', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')])),
                ('perfil_cultura', models.ForeignKey(default=None, blank=True, to='cultura_empresarial.Perfil_Cultura', null=True)),
                ('pregunta', models.ForeignKey(default=None, blank=True, to='cultura_empresarial.PreguntaCultura', null=True)),
            ],
            options={
                'ordering': ['pregunta', 'orden'],
            },
        ),
        migrations.AddField(
            model_name='culturamatrizdisc',
            name='perfil_cultura',
            field=models.ForeignKey(default=None, blank=True, to='cultura_empresarial.Perfil_Cultura', null=True),
        ),
    ]
