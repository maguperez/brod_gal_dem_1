# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaEmpresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=b'50')),
                ('fecha_creacion', models.DateField(default=None, null=True, blank=True)),
                ('fecha_modificacion', models.DateField(default=None, null=True, blank=True)),
                ('estado', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')])),
                ('orden', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'ordering': ['orden'],
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(default=None, max_length=b'100', null=True, blank=True)),
                ('descripcion', models.CharField(default=None, max_length=b'200', null=True, blank=True)),
                ('quienes_somos', models.CharField(default=None, max_length=b'1000', null=True, blank=True)),
                ('telefono', models.CharField(default=None, max_length=b'100', null=True, blank=True)),
                ('RUC', models.CharField(default=None, max_length=b'20', null=True, blank=True)),
                ('ano_fundacion', models.CharField(default=None, max_length=b'10', null=True, blank=True)),
                ('website', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('logo', models.ImageField(upload_to=b'img/%Y/%m/%d', null=True, verbose_name=b'logo', blank=True)),
                ('direccion_map', models.CharField(default=None, max_length=b'100', null=True, blank=True)),
                ('longitud', models.FloatField(default=None, null=True, verbose_name=b'longitud', blank=True)),
                ('latitud', models.FloatField(default=None, null=True, verbose_name=b'latitud', blank=True)),
                ('usuario_creacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_creacion', models.DateField(default=None, null=True, blank=True)),
                ('usuario_modificacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_modificacion', models.DateField(default=None, null=True, blank=True)),
                ('estado', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')])),
                ('ciudad', models.ForeignKey(default=None, blank=True, to='main.Ciudad', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa_Imagenes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.ImageField(default=None, null=True, upload_to=b'img/%Y/%m/%d', blank=True)),
                ('slug', models.SlugField(blank=True)),
                ('usuario_creacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_creacion', models.DateField(default=None, null=True, blank=True)),
                ('usuario_modificacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_modificacion', models.DateField(default=None, null=True, blank=True)),
                ('estado', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')])),
                ('empresa', models.ForeignKey(default=None, blank=True, to='empresa.Empresa', null=True)),
            ],
        ),
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
        migrations.CreateModel(
            name='EvaluacionEmpresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('linea_carrera', models.FloatField(default=None, null=True, blank=True)),
                ('flexibilidad_horarios', models.FloatField(default=None, null=True, blank=True)),
                ('ambiente_trabajo', models.FloatField(default=None, null=True, blank=True)),
                ('salarios', models.FloatField(default=None, null=True, blank=True)),
                ('ranking', models.FloatField(default=None, null=True, blank=True)),
                ('usuario_creacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_creacion', models.DateField(default=None, null=True, blank=True)),
                ('usuario_modificacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_modificacion', models.DateField(default=None, null=True, blank=True)),
                ('estado', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')])),
                ('empresa', models.ForeignKey(to='empresa.Empresa')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FacturacionAnual',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=b'50')),
                ('fecha_creacion', models.DateField(default=None, null=True, blank=True)),
                ('fecha_modificacion', models.DateField(default=None, null=True, blank=True)),
                ('estado', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')])),
                ('orden', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'ordering': ['orden'],
            },
        ),
        migrations.CreateModel(
            name='NumeroFuncionarios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=b'50')),
                ('fecha_creacion', models.DateField(default=None, null=True, blank=True)),
                ('fecha_modificacion', models.DateField(default=None, null=True, blank=True)),
                ('estado', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')])),
                ('orden', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'ordering': ['orden'],
            },
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.ImageField(upload_to=b'pictures')),
                ('slug', models.SlugField(blank=True)),
                ('empresa', models.ForeignKey(default=None, blank=True, to='empresa.Empresa', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Puesto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=b'50')),
                ('orden', models.IntegerField(null=True, blank=True)),
                ('fecha_creacion', models.DateField(default=None, null=True, blank=True)),
                ('fecha_modificacion', models.DateField(default=None, null=True, blank=True)),
                ('estado', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')])),
            ],
            options={
                'ordering': ['orden'],
            },
        ),
        migrations.CreateModel(
            name='RankingEmpresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('linea_carrera', models.FloatField(default=None, null=True, blank=True)),
                ('flexibilidad_horarios', models.FloatField(default=None, null=True, blank=True)),
                ('ambiente_trabajo', models.FloatField(default=None, null=True, blank=True)),
                ('salarios', models.FloatField(default=None, null=True, blank=True)),
                ('ranking_general', models.FloatField(default=None, null=True, blank=True)),
                ('usuario_creacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_creacion', models.DateField(default=None, null=True, blank=True)),
                ('usuario_modificacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_modificacion', models.DateField(default=None, null=True, blank=True)),
                ('estado', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')])),
                ('empresa', models.ForeignKey(to='empresa.Empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Representante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('usuario_creacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_creacion', models.DateField(default=None, null=True, blank=True)),
                ('usuario_modificacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_modificacion', models.DateField(default=None, null=True, blank=True)),
                ('estado', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')])),
                ('empresa', models.ForeignKey(to='empresa.Empresa')),
                ('persona', models.OneToOneField(to='main.Persona')),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=b'50')),
                ('fecha_creacion', models.DateField(default=None, null=True, blank=True)),
                ('fecha_modificacion', models.DateField(default=None, null=True, blank=True)),
                ('estado', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')])),
                ('orden', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'ordering': ['orden'],
            },
        ),
        migrations.CreateModel(
            name='VideoUrl',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(default=None, null=True, blank=True)),
                ('empresa', models.ForeignKey(default=None, blank=True, to='empresa.Empresa', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='empresa',
            name='facturacion_anual',
            field=models.ForeignKey(default=None, blank=True, to='empresa.FacturacionAnual', null=True),
        ),
        migrations.AddField(
            model_name='empresa',
            name='numero_funcionarios',
            field=models.ForeignKey(default=None, blank=True, to='empresa.NumeroFuncionarios', null=True),
        ),
        migrations.AddField(
            model_name='empresa',
            name='pais',
            field=models.ForeignKey(default=None, blank=True, to='main.Pais', null=True),
        ),
        migrations.AddField(
            model_name='empresa',
            name='sector',
            field=models.ForeignKey(default=None, blank=True, to='empresa.Sector', null=True),
        ),
    ]
