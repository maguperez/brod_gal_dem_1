# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oportunidad', '0007_auto_20151117_1138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfiloportunidad',
            name='ciudad',
        ),
        migrations.RemoveField(
            model_name='perfiloportunidad',
            name='pais',
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
            name='remuneracion',
            field=models.ForeignKey(default=None, blank=True, to='main.TipoRemuneracion', null=True, verbose_name=b'Remuneracion'),
        ),
        migrations.AlterField(
            model_name='oportunidad',
            name='tipo_puesto',
            field=models.ForeignKey(default=None, blank=True, to='main.TipoPuesto', null=True, verbose_name=b'Tipo Puesto'),
        ),
    ]
