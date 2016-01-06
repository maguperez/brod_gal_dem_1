# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0020_picture_empresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='usuario_creacion',
            field=models.CharField(default=None, max_length=b'50', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='empresa_imagenes',
            name='fecha_modificacion',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='empresa_imagenes',
            name='usuario_creacion',
            field=models.CharField(default=None, max_length=b'50', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='evaluacionempresa',
            name='usuario_creacion',
            field=models.CharField(default=None, max_length=b'50', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='evaluacionempresa',
            name='usuario_modificacion',
            field=models.CharField(default=None, max_length=b'50', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='rankingempresa',
            name='usuario_creacion',
            field=models.CharField(default=None, max_length=b'50', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='rankingempresa',
            name='usuario_modificacion',
            field=models.CharField(default=None, max_length=b'50', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='representante',
            name='usuario_creacion',
            field=models.CharField(default=None, max_length=b'50', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='representante',
            name='usuario_modificacion',
            field=models.CharField(default=None, max_length=b'50', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='usuario_modificacion',
            field=models.CharField(default=None, max_length=b'50', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='empresa_imagenes',
            name='usuario_modificacion',
            field=models.CharField(default=None, max_length=b'50', null=True, blank=True),
        ),
    ]
