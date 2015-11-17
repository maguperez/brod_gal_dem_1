# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_beneficio_tiporemuneracion'),
        ('oportunidad', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='oportunidad',
            name='beneficio',
            field=models.ForeignKey(default=None, blank=True, to='main.Beneficio', null=True),
        ),
        migrations.AlterField(
            model_name='oportunidad',
            name='tipo_puesto',
            field=models.ForeignKey(default=None, blank=True, to='main.TipoPuesto', null=True),
        ),
    ]
