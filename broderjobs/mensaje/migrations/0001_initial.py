# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('oportunidad', '0023_oportunidad_usuario'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('asunto', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('contenido', models.CharField(default=None, max_length=1000, null=True, blank=True)),
                ('permite_respuesta', models.BooleanField(default=False)),
                ('fecha_creacion', models.DateField(default=None, null=True, blank=True)),
                ('fecha_modificacion', models.DateField(default=None, null=True, blank=True)),
                ('estado', models.CharField(default=None, max_length=1, null=True, blank=True, choices=[(b'G', b'Guardado'), (b'E', b'Eliminado')])),
                ('postulacion', models.ForeignKey(default=None, blank=True, to='oportunidad.Postulacion', null=True)),
                ('usuario_remitente', models.ForeignKey(default=None, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mensaje_Destinatario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('leido', models.BooleanField(default=False)),
                ('fecha_leido', models.DateField(default=None, null=True, blank=True)),
                ('fecha_modificacion', models.DateField(default=None, null=True, blank=True)),
                ('estado', models.CharField(default=None, max_length=1, null=True, blank=True, choices=[(b'G', b'Guardado'), (b'E', b'Eliminado')])),
                ('mensaje', models.ForeignKey(default=None, blank=True, to='mensaje.Mensaje', max_length=1000, null=True)),
                ('usuario_destinatario', models.ForeignKey(default=None, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
