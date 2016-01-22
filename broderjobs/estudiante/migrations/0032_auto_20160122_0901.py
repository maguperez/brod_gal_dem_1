# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0031_auto_20160122_0816'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConocimientoExtra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('orden', models.IntegerField(null=True, blank=True)),
                ('fecha_creacion', models.DateField(default=None, null=True, blank=True)),
                ('fecha_modificacion', models.DateField(default=None, null=True, blank=True)),
                ('estado', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')])),
            ],
            options={
                'ordering': ['orden'],
            },
        ),
        migrations.RenameField(
            model_name='estudiante',
            old_name='test_completo',
            new_name='completo_test',
        ),
        migrations.AddField(
            model_name='conocimientoextra',
            name='estudiante',
            field=models.ForeignKey(default=None, blank=True, to='estudiante.Estudiante', null=True),
        ),
    ]
