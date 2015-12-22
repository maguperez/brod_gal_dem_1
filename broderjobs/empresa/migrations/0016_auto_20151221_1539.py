# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0015_auto_20151218_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa_imagenes',
            name='imagen',
            field=models.ImageField(null=True, upload_to=b'img/%Y/%m/%d', blank=True),
        ),
    ]
