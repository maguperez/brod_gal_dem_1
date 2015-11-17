# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oportunidad', '0004_auto_20151116_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oportunidad',
            name='carga_horaria',
            field=models.ForeignKey(blank=True, to='main.CargaHoraria', null=True),
        ),
        migrations.AlterField(
            model_name='oportunidad',
            name='ciudad',
            field=models.ForeignKey(blank=True, to='main.Ciudad', null=True),
        ),
        migrations.AlterField(
            model_name='oportunidad',
            name='fecha_cese',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='oportunidad',
            name='pais',
            field=models.ForeignKey(blank=True, to='main.Pais', null=True),
        ),
        migrations.AlterField(
            model_name='oportunidad',
            name='remuneracion',
            field=models.ForeignKey(blank=True, to='main.TipoRemuneracion', null=True),
        ),
        migrations.AlterField(
            model_name='oportunidad',
            name='tipo_puesto',
            field=models.ForeignKey(blank=True, to='main.TipoPuesto', null=True),
        ),
    ]
