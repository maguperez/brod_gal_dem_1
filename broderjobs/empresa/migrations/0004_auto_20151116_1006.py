# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_beneficio_tiporemuneracion'),
        ('empresa', '0003_auto_20151115_2033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='SedeGlobal',
        ),
        migrations.AddField(
            model_name='empresa',
            name='ciudad',
            field=models.ForeignKey(default=None, blank=True, to='main.Ciudad', null=True),
        ),
        migrations.AddField(
            model_name='empresa',
            name='logo',
            field=models.ImageField(upload_to=b'img/%Y/%m/%d', null=True, verbose_name=b'logo', blank=True),
        ),
        migrations.AddField(
            model_name='empresa',
            name='pais',
            field=models.ForeignKey(default=None, blank=True, to='main.Pais', null=True),
        ),
    ]
