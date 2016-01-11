# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0021_auto_20160106_1429'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmpresaRedesSociales',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('facebook', models.CharField(default=None, max_length=b'200', null=True, blank=True)),
                ('twitter', models.CharField(default=None, max_length=b'200', null=True, blank=True)),
                ('linkedin', models.CharField(default=None, max_length=b'200', null=True, blank=True)),
                ('usuario_creacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_creacion', models.DateField(default=None, null=True, blank=True)),
                ('usuario_modificacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_modificacion', models.DateField(default=None, null=True, blank=True)),
                ('estado', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')])),
                ('empresa', models.ForeignKey(to='empresa.Empresa')),
            ],
        ),
    ]
