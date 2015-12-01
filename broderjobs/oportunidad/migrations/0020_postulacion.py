# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0021_auto_20151116_2347'),
        ('oportunidad', '0019_auto_20151127_1015'),
    ]

    operations = [
        migrations.CreateModel(
            name='Postulacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Fecha', models.DateField(default=None, null=True, blank=True)),
                ('Estudiante', models.ForeignKey(default=None, blank=True, to='estudiante.Estudiante', null=True)),
                ('Oportunidad', models.ForeignKey(default=None, blank=True, to='oportunidad.Oportunidad', null=True)),
            ],
        ),
    ]
