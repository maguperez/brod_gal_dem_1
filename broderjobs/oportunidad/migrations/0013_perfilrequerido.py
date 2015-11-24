# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oportunidad', '0012_remove_perfiloportunidad_grado_estudio'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerfilRequerido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('perfil', models.CharField(default=None, max_length=b'10', null=True, blank=True)),
            ],
        ),
    ]
