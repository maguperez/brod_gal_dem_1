# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0023_empresa_telefono'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoriaempresa',
            options={'ordering': ['orden']},
        ),
        migrations.AlterModelOptions(
            name='facturacionanual',
            options={'ordering': ['orden']},
        ),
        migrations.AlterModelOptions(
            name='numerofuncionarios',
            options={'ordering': ['orden']},
        ),
        migrations.AlterModelOptions(
            name='puesto',
            options={'ordering': ['orden']},
        ),
        migrations.AlterModelOptions(
            name='sector',
            options={'ordering': ['orden']},
        ),
        migrations.AddField(
            model_name='categoriaempresa',
            name='orden',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='facturacionanual',
            name='orden',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='numerofuncionarios',
            name='orden',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='puesto',
            name='orden',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='sector',
            name='orden',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
