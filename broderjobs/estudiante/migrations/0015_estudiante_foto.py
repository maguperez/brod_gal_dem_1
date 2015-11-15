# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0014_auto_20151113_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='foto',
            field=models.ImageField(upload_to=b'/img/%Y/%m/%d', null=True, verbose_name=b'foto perfil', blank=True),
        ),
    ]
