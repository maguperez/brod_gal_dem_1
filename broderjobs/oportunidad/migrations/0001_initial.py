# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_beneficio_tiporemuneracion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oportunidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(default=None, max_length=b'100', null=True, blank=True)),
                ('remuneracion_min', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('remuneracion_max', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_cese', models.DateField(null=True)),
                ('carga', models.ForeignKey(default=None, blank=True, to='main.CargaHoraria', null=True)),
                ('ciudad', models.ForeignKey(default=None, blank=True, to='main.Ciudad', null=True)),
                ('pais', models.ForeignKey(default=None, blank=True, to='main.Pais', null=True)),
                ('remuneracion', models.ForeignKey(default=None, blank=True, to='main.TipoRemuneracion', null=True)),
                ('tipo_puesto', models.ForeignKey(default=None, verbose_name=b'Tipo Puesto', blank=True, to='main.TipoPuesto')),
            ],
        ),
    ]
