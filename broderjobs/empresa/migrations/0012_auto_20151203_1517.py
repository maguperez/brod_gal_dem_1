# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('empresa', '0011_auto_20151125_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoriaempresa',
            name='estado',
            field=models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')]),
        ),
        migrations.AddField(
            model_name='categoriaempresa',
            name='fecha_creacion',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='categoriaempresa',
            name='fecha_modificacion',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='empresa',
            name='estado',
            field=models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')]),
        ),
        migrations.AddField(
            model_name='empresa',
            name='fecha_creacion',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='empresa',
            name='fecha_modificacion',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='empresa',
            name='usuario_modificacion',
            field=models.ForeignKey(default=None, blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='facturacionanual',
            name='estado',
            field=models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')]),
        ),
        migrations.AddField(
            model_name='facturacionanual',
            name='fecha_creacion',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='facturacionanual',
            name='fecha_modificacion',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='imagensilder',
            name='estado',
            field=models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')]),
        ),
        migrations.AddField(
            model_name='imagensilder',
            name='fecha_creacion',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='imagensilder',
            name='fecha_modificacion',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='imagensilder',
            name='usuario_modificacion',
            field=models.ForeignKey(default=None, blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='numerofuncionarios',
            name='estado',
            field=models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')]),
        ),
        migrations.AddField(
            model_name='numerofuncionarios',
            name='fecha_creacion',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='numerofuncionarios',
            name='fecha_modificacion',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='puesto',
            name='estado',
            field=models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')]),
        ),
        migrations.AddField(
            model_name='puesto',
            name='fecha_creacion',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='puesto',
            name='fecha_modificacion',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='representante',
            name='estado',
            field=models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')]),
        ),
        migrations.AddField(
            model_name='representante',
            name='fecha_creacion',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='representante',
            name='fecha_modificacion',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='sector',
            name='estado',
            field=models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')]),
        ),
        migrations.AddField(
            model_name='sector',
            name='fecha_creacion',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='sector',
            name='fecha_modificacion',
            field=models.DateField(default=None, null=True, blank=True),
        ),
    ]
