# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disc', '0007_auto_20160127_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudianterespuestas',
            name='patron',
            field=models.CharField(default=None, max_length=b'50', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='estudianterespuestas',
            name='total_c',
            field=models.IntegerField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='estudianterespuestas',
            name='total_d',
            field=models.IntegerField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='estudianterespuestas',
            name='total_i',
            field=models.IntegerField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='estudianterespuestas',
            name='total_s',
            field=models.IntegerField(default=None, null=True, blank=True),
        ),
    ]
