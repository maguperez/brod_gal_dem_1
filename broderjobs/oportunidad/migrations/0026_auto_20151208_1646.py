# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oportunidad', '0025_auto_20151204_0832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oportunidad',
            name='beneficio',
        ),
        migrations.RemoveField(
            model_name='oportunidad',
            name='carga_horaria',
        ),
        migrations.RemoveField(
            model_name='oportunidad',
            name='carrera',
        ),
        migrations.RemoveField(
            model_name='oportunidad',
            name='ciudad',
        ),
        migrations.RemoveField(
            model_name='oportunidad',
            name='conocimiento',
        ),
        migrations.RemoveField(
            model_name='oportunidad',
            name='direccion_map',
        ),
        migrations.RemoveField(
            model_name='oportunidad',
            name='empresa',
        ),
        migrations.RemoveField(
            model_name='oportunidad',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='oportunidad',
            name='estado_opotunidad',
        ),
        migrations.RemoveField(
            model_name='oportunidad',
            name='fecha_cese',
        ),
        migrations.RemoveField(
            model_name='oportunidad',
            name='fecha_creacion',
        ),
        migrations.RemoveField(
            model_name='oportunidad',
            name='fecha_modificacion',
        ),
        migrations.RemoveField(
            model_name='oportunidad',
            name='fecha_publicacion',
        ),
        migrations.RemoveField(
            model_name='oportunidad',
            name='grado_estudio',
        ),
        migrations.RemoveField(
            model_name='oportunidad',
            name='idioma',
        ),
        migrations.RemoveField(
            model_name='oportunidad',
            name='latitud',
        ),
        migrations.RemoveField(
            model_name='oportunidad',
            name='longitud',
        ),
        migrations.RemoveField(
            model_name='oportunidad',
            name='pais',
        ),
        migrations.RemoveField(
            model_name='oportunidad',
            name='remuneracion',
        ),
        migrations.RemoveField(
            model_name='oportunidad',
            name='remuneracion_max',
        ),
        migrations.RemoveField(
            model_name='oportunidad',
            name='remuneracion_min',
        ),
        migrations.RemoveField(
            model_name='oportunidad',
            name='resumen',
        ),
        migrations.RemoveField(
            model_name='oportunidad',
            name='tipo_puesto',
        ),
        migrations.RemoveField(
            model_name='oportunidad',
            name='universidad',
        ),
        migrations.RemoveField(
            model_name='oportunidad',
            name='usuario',
        ),
    ]
