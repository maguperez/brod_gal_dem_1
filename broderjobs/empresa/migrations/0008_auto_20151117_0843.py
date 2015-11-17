# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0007_auto_20151116_1328'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagenSilder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=b'50')),
                ('imagen', models.ImageField(upload_to=b'img/%Y/%m/%d', null=True, verbose_name=b'imagen', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='empresa',
            name='imagen_slider',
            field=models.ManyToManyField(default=None, to='empresa.ImagenSilder', verbose_name=b'Imagenes', blank=True),
        ),
    ]
