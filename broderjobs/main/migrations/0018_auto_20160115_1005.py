# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20160115_0814'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeriodosGraduacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('valor', models.IntegerField(null=True, blank=True)),
                ('orden', models.IntegerField(null=True, blank=True)),
                ('fecha_creacion', models.DateField(default=None, null=True, blank=True)),
                ('fecha_modificacion', models.DateField(default=None, null=True, blank=True)),
                ('estado', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')])),
            ],
        ),
        migrations.DeleteModel(
            name='PeriodoGraduacion',
        ),
        migrations.AlterModelOptions(
            name='beneficio',
            options={'ordering': ['orden']},
        ),
        migrations.AlterModelOptions(
            name='cargahoraria',
            options={'ordering': ['orden']},
        ),
        migrations.AlterModelOptions(
            name='carrera',
            options={'ordering': ['orden']},
        ),
        migrations.AlterModelOptions(
            name='ciudad',
            options={'ordering': ['orden']},
        ),
        migrations.AlterModelOptions(
            name='conocimiento',
            options={'ordering': ['orden']},
        ),
        migrations.AlterModelOptions(
            name='gradoestudio',
            options={'ordering': ['orden']},
        ),
        migrations.AlterModelOptions(
            name='idioma',
            options={'ordering': ['orden']},
        ),
        migrations.AlterModelOptions(
            name='pais',
            options={'ordering': ['orden']},
        ),
        migrations.AlterModelOptions(
            name='tipopuesto',
            options={'ordering': ['orden']},
        ),
        migrations.AlterModelOptions(
            name='tiporemuneracion',
            options={'ordering': ['orden']},
        ),
        migrations.AlterModelOptions(
            name='universidad',
            options={'ordering': ['orden']},
        ),
    ]
