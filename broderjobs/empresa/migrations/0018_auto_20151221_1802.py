# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0017_auto_20151221_1539'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empresa_imagenes',
            old_name='imagen',
            new_name='file',
        ),
    ]
