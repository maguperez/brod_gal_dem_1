# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0016_auto_20151221_1539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa_imagenes',
            name='empresa',
        ),
        migrations.AddField(
            model_name='empresa_imagenes',
            name='empresa',
            field=models.ForeignKey(default=None, blank=True, to='empresa.Empresa', null=True),
        ),
        migrations.AlterField(
            model_name='empresa_imagenes',
            name='imagen',
            field=models.ImageField(default=None, null=True, upload_to=b'img/%Y/%m/%d', blank=True),
        ),
    ]
