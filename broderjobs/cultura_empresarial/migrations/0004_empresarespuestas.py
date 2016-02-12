# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0025_videourl'),
        ('cultura_empresarial', '0003_auto_20160212_1351'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmpresaRespuestas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('orden', models.IntegerField(default=None, null=True, blank=True)),
                ('usuario_creacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_creacion', models.DateField(default=datetime.datetime.now, null=True, blank=True)),
                ('usuario_modificacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_modificacion', models.DateField(default=datetime.datetime.now, null=True, blank=True)),
                ('estado', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')])),
                ('empresa', models.ForeignKey(default=None, blank=True, to='empresa.Empresa', null=True)),
                ('pregunta', models.ForeignKey(default=None, blank=True, to='cultura_empresarial.PreguntaCultura', null=True)),
                ('respuesta', models.ForeignKey(default=None, blank=True, to='cultura_empresarial.RespuestaCultura', null=True)),
            ],
            options={
                'ordering': ['empresa', 'pregunta', 'orden'],
            },
        ),
    ]
