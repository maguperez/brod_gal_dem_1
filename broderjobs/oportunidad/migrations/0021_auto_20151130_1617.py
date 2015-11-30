# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oportunidad', '0020_postulacion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postulacion',
            old_name='Estudiante',
            new_name='estudiante',
        ),
        migrations.RenameField(
            model_name='postulacion',
            old_name='Fecha',
            new_name='fecha',
        ),
        migrations.RenameField(
            model_name='postulacion',
            old_name='Oportunidad',
            new_name='oportunidad',
        ),
    ]
