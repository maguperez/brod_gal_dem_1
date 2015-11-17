# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0002_auto_20151115_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='facturacion_anual',
            field=models.ForeignKey(default=None, blank=True, to='empresa.FacturacionAnual', null=True),
        ),
        migrations.AddField(
            model_name='empresa',
            name='numero_funcioarios',
            field=models.ForeignKey(default=None, blank=True, to='empresa.NumeroFuncionarios', null=True),
        ),
        migrations.AddField(
            model_name='empresa',
            name='sector',
            field=models.ForeignKey(default=None, blank=True, to='empresa.Sector', null=True),
        ),
    ]
