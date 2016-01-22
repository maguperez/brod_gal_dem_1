# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatronPerfil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nro_patron', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
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
            name='Perfil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
        migrations.AlterModelOptions(
            name='pregunta',
            options={'ordering': ['orden']},
        ),
        migrations.AlterModelOptions(
            name='respuesta',
            options={'ordering': ['pregunta', 'orden']},
        ),
        migrations.AlterField(
            model_name='respuestaestudiante',
            name='descripcion',
            field=models.CharField(default=None, max_length=b'200', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='patronperfil',
            name='perfil',
            field=models.ForeignKey(default=None, blank=True, to='disc.Perfil', null=True),
        ),
    ]
