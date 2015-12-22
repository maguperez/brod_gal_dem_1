# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0019_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='empresa',
            field=models.ForeignKey(default=None, blank=True, to='empresa.Empresa', null=True),
        ),
    ]
