# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20160120_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='genero',
            field=models.CharField(default=b'', max_length=1, null=True, blank=True, choices=[(b'M', b'Masculino'), (b'F', b'Femenino')]),
        ),
    ]
