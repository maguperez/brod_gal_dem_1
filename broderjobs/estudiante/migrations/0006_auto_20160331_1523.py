# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0005_auto_20160331_1400'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiante',
            name='foto_facebook',
        ),
        migrations.AddField(
            model_name='estudiante',
            name='foto_facebook_url',
            field=models.URLField(default=None, null=True, blank=True),
        ),
    ]
