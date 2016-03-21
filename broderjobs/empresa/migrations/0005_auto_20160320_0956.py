# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0004_auto_20160310_1010'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empresa',
            options={'ordering': ['orden']},
        ),
        migrations.AlterModelOptions(
            name='sector',
            options={'ordering': ['descripcion']},
        ),
        migrations.AddField(
            model_name='empresa',
            name='orden',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
