# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20160105_0805'),
    ]

    operations = [
        migrations.AddField(
            model_name='beneficio',
            name='orden',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='cargahoraria',
            name='orden',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='carrera',
            name='orden',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='orden',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='conocimiento',
            name='orden',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='gradoestudio',
            name='orden',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='idioma',
            name='orden',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='pais',
            name='orden',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tipopuesto',
            name='orden',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tiporemuneracion',
            name='orden',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='universidad',
            name='orden',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
