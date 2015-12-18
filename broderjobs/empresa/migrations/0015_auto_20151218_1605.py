# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('empresa', '0014_auto_20151214_0838'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa_Imagenes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagen', models.ImageField(upload_to=b'img/%Y/%m/%d')),
                ('slug', models.SlugField(blank=True)),
                ('fecha_creacion', models.DateField(default=None, null=True, blank=True)),
                ('estado', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')])),
            ],
        ),
        migrations.RemoveField(
            model_name='imagensilder',
            name='usuario_modificacion',
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='imagen_slider',
        ),
        migrations.DeleteModel(
            name='ImagenSilder',
        ),
        migrations.AddField(
            model_name='empresa_imagenes',
            name='empresa',
            field=models.ManyToManyField(default=None, to='empresa.Empresa', verbose_name=b'Imagenes', blank=True),
        ),
        migrations.AddField(
            model_name='empresa_imagenes',
            name='usuario_modificacion',
            field=models.ForeignKey(default=None, blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
