# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0022_empresaredessociales'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='telefono',
            field=models.CharField(default=None, max_length=b'100', null=True, blank=True),
        ),
    ]
