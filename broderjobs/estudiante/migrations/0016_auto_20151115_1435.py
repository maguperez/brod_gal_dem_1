# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0015_estudiante_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='foto',
            field=models.ImageField(upload_to=b'img/%Y/%m/%d', null=True, verbose_name=b'foto perfil', blank=True),
        ),
        migrations.AlterField(
            model_name='resumen',
            name='descripcion',
            field=models.CharField(default=None, max_length=b'1000', null=True, blank=True),
        ),
    ]
