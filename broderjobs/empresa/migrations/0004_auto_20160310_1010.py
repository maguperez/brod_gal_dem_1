# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0003_auto_20160305_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='nombre',
            field=models.CharField(default=None, max_length=b'1000', null=True, blank=True),
        ),
    ]
