# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_cargahoraria_idioma_tipopuesto'),
        ('estudiante', '0008_auto_20151112_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='carga_horaria',
            field=models.ForeignKey(to='main.CargaHoraria', null=True),
        ),
        migrations.AlterField(
            model_name='actividadesextra',
            name='descripcion',
            field=models.CharField(default=None, max_length=b'50', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='actividadesextra',
            name='organizacion',
            field=models.CharField(default=None, max_length=b'50', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='resumen',
            name='descripcion',
            field=models.CharField(default=None, max_length=b'100', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='voluntariado',
            name='cargo',
            field=models.CharField(default=None, max_length=b'50', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='voluntariado',
            name='descripcion',
            field=models.CharField(default=None, max_length=b'100', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='voluntariado',
            name='organizacion',
            field=models.CharField(default=None, max_length=b'50', null=True, blank=True),
        ),
    ]
