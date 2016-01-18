# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20160115_1005'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='periodosgraduacion',
            options={'ordering': ['orden']},
        ),
    ]
