# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        # ('oportunidad', '0032_auto_20160111_1506'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mensaje', '0004_auto_20160107_0904'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notificacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('asunto', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('fecha_leido', models.DateField(default=None, null=True, blank=True)),
                ('es_mensaje', models.BooleanField(default=False)),
                ('fecha_creacion', models.DateField(default=None, null=True, blank=True)),
                ('fecha_modificacion', models.DateField(default=None, null=True, blank=True)),
                ('estado', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')])),
                ('oportunidad', models.ForeignKey(default=None, blank=True, to='oportunidad.Oportunidad', null=True)),
                ('usuario_destinatario', models.ForeignKey(default=None, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
