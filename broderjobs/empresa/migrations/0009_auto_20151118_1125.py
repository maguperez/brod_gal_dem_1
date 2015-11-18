# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0008_auto_20151117_0843'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaEmpresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=b'50')),
            ],
        ),
        migrations.AddField(
            model_name='empresa',
            name='quienes_somos',
            field=models.CharField(default=None, max_length=b'1000', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='empresa',
            name='ranking_general',
            field=models.CharField(default=None, max_length=b'10', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='imagensilder',
            name='url',
            field=models.CharField(default=None, max_length=b'1000', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='descripcion',
            field=models.CharField(default=None, max_length=b'200', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='imagensilder',
            name='titulo',
            field=models.CharField(default=None, max_length=b'50', null=True, blank=True),
        ),
    ]
