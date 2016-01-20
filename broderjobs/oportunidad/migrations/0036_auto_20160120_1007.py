# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oportunidad', '0035_auto_20160118_1130'),
    ]

    operations = [
        migrations.CreateModel(
            name='BeneficioExtra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('orden', models.IntegerField(null=True, blank=True)),
                ('fecha_creacion', models.DateField(default=None, null=True, blank=True)),
                ('fecha_modificacion', models.DateField(default=None, null=True, blank=True)),
                ('estado', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')])),
            ],
            options={
                'ordering': ['orden'],
            },
        ),
        # migrations.RemoveField(
        #     model_name='oportunidad',
        #     name='estado_opotunidad',
        # ),
        # migrations.AddField(
        #     model_name='oportunidad',
        #     name='estado_oportunidad',
        #     field=models.CharField(default=None, max_length=1, null=True, blank=True, choices=[(b'P', b'Archivado'), (b'A', b'Abierto'), (b'C', b'Cerrado')]),
        # ),
        migrations.AddField(
            model_name='beneficioextra',
            name='oportunidad',
            field=models.ForeignKey(default=None, blank=True, to='oportunidad.Oportunidad', null=True),
        ),
    ]
