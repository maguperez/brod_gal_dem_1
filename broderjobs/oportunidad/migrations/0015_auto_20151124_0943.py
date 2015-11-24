# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oportunidad', '0014_auto_20151124_0940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oportunidad',
            name='perfil_oportunidad',
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='perfil_requerido',
            field=models.ForeignKey(default=None, blank=True, to='oportunidad.PerfilRequerido', null=True),
        ),
        migrations.DeleteModel(
            name='PerfilOportunidad',
        ),
    ]
