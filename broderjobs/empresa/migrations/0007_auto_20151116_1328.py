# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0006_auto_20151116_1323'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empresa',
            old_name='numero_funcioarios',
            new_name='numero_funcionarios',
        ),
    ]
