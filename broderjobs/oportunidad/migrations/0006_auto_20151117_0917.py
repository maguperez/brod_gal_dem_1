# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_beneficio_tiporemuneracion'),
        ('oportunidad', '0005_auto_20151117_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfilcandidato',
            name='conocimiento',
            field=models.ManyToManyField(default=None, to='main.Conocimiento', verbose_name=b'Conocimiento', blank=True),
        ),
        migrations.AlterField(
            model_name='oportunidad',
            name='beneficio',
            field=models.ForeignKey(default=None, blank=True, to='main.Beneficio', null=True, verbose_name=b'Beneficio'),
        ),
        migrations.AlterField(
            model_name='oportunidad',
            name='carga_horaria',
            field=models.ForeignKey(default=None, blank=True, to='main.CargaHoraria', null=True, verbose_name=b'Jornada Laboral'),
        ),
        migrations.AlterField(
            model_name='oportunidad',
            name='tipo_puesto',
            field=models.ForeignKey(default=None, blank=True, to='main.TipoPuesto', null=True, verbose_name=b'Tipo Puesto'),
        ),
    ]
