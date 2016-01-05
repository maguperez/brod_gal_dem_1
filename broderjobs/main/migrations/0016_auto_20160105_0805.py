# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20151208_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='universidad',
            name='nemonico',
            field=models.CharField(default=None, max_length=b'50', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='universidad',
            name='pais',
            field=models.ForeignKey(default=None, blank=True, to='main.Pais', null=True),
        ),
    ]
