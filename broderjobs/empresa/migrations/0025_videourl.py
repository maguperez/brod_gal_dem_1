# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0024_auto_20160115_0841'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoUrl',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(default=None, null=True, blank=True)),
                ('empresa', models.ForeignKey(default=None, blank=True, to='empresa.Empresa', null=True)),
            ],
        ),
    ]
