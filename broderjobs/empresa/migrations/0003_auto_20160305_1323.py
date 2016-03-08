# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0002_representante_administrador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoriaempresa',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='categoriaempresa',
            name='fecha_modificacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='fecha_modificacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='empresa_imagenes',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='empresa_imagenes',
            name='fecha_modificacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='empresaredessociales',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='empresaredessociales',
            name='fecha_modificacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='evaluacionempresa',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='evaluacionempresa',
            name='fecha_modificacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='facturacionanual',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='facturacionanual',
            name='fecha_modificacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='numerofuncionarios',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='numerofuncionarios',
            name='fecha_modificacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='puesto',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='puesto',
            name='fecha_modificacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rankingempresa',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rankingempresa',
            name='fecha_modificacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='representante',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='representante',
            name='fecha_modificacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='sector',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='sector',
            name='fecha_modificacion',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
    ]
