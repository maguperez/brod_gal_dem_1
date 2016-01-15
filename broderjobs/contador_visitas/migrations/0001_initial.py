# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oportunidad', '0033_auto_20160112_0817'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitasOportunidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.CharField(default=None, max_length=b'100', null=True, blank=True)),
                ('usuario_creacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_creacion', models.DateField(default=None, null=True, blank=True)),
                ('estado', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')])),
                ('oportunidad', models.ForeignKey(default=None, blank=True, to='oportunidad.Oportunidad', null=True)),
            ],
        ),
    ]
