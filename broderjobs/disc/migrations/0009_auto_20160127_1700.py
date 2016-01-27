# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disc', '0008_auto_20160127_1638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudianterespuestas',
            name='patron',
        ),
        migrations.RemoveField(
            model_name='estudianterespuestas',
            name='total_c',
        ),
        migrations.RemoveField(
            model_name='estudianterespuestas',
            name='total_d',
        ),
        migrations.RemoveField(
            model_name='estudianterespuestas',
            name='total_i',
        ),
        migrations.RemoveField(
            model_name='estudianterespuestas',
            name='total_s',
        ),
        migrations.AddField(
            model_name='estudiantepatron',
            name='patron',
            field=models.CharField(default=None, max_length=b'50', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='estudiantepatron',
            name='total_c',
            field=models.IntegerField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='estudiantepatron',
            name='total_d',
            field=models.IntegerField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='estudiantepatron',
            name='total_i',
            field=models.IntegerField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='estudiantepatron',
            name='total_s',
            field=models.IntegerField(default=None, null=True, blank=True),
        ),
    ]
