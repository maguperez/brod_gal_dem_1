# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disc', '0005_auto_20160127_0929'),
    ]

    operations = [
        migrations.AddField(
            model_name='disccodificacion',
            name='valor',
            field=models.IntegerField(default=None, null=True, blank=True),
        ),
    ]
