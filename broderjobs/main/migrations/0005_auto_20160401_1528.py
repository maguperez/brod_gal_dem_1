# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20160331_1417'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carrera',
            options={'ordering': ['orden', 'descripcion']},
        ),
        migrations.AlterModelOptions(
            name='tipocarrera',
            options={'ordering': ['orden', 'descripcion']},
        ),
        migrations.AlterModelOptions(
            name='tipopuesto',
            options={'ordering': ['orden', 'descripcion']},
        ),
    ]
