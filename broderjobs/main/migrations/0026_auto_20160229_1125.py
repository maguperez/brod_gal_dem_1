# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_auto_20160128_1005'),
    ]

    operations = [
        migrations.CreateModel(
            name='IdiomaBase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('orden', models.IntegerField(null=True, blank=True)),
                ('fecha_creacion', models.DateField(default=datetime.datetime.now, null=True, blank=True)),
                ('fecha_modificacion', models.DateField(default=datetime.datetime.now, null=True, blank=True)),
                ('estado', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')])),
            ],
            options={
                'ordering': ['orden'],
            },
        ),
        migrations.AddField(
            model_name='idioma',
            name='idiomabase',
            field=models.ForeignKey(default=None, blank=True, to='main.IdiomaBase', null=True),
        ),
    ]
