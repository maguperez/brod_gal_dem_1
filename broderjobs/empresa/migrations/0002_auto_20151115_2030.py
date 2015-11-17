# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_conocimiento'),
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacturacionAnual',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=b'50')),
            ],
        ),
        migrations.CreateModel(
            name='NumeroFuncionarios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=b'50')),
            ],
        ),
        migrations.CreateModel(
            name='Representante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=b'50')),
            ],
        ),
        migrations.AddField(
            model_name='empresa',
            name='RUC',
            field=models.CharField(default=None, max_length=b'20', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='empresa',
            name='SedeGlobal',
            field=models.CharField(default=None, max_length=b'100', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='empresa',
            name='ano_fundacion',
            field=models.CharField(default=None, max_length=b'10', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='empresa',
            name='nombre',
            field=models.CharField(default=None, max_length=b'100', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='empresa',
            name='website',
            field=models.CharField(default=None, max_length=b'50', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='descripcion',
            field=models.CharField(default=None, max_length=b'1000', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='representante',
            name='empresa',
            field=models.ForeignKey(to='empresa.Empresa'),
        ),
        migrations.AddField(
            model_name='representante',
            name='persona',
            field=models.OneToOneField(to='main.Persona'),
        ),
    ]
