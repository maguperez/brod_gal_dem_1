# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0007_resumen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actividadesextra',
            old_name='Estudiante',
            new_name='estudiante',
        ),
        migrations.RenameField(
            model_name='experienciaprofesional',
            old_name='Estudiante',
            new_name='estudiante',
        ),
        migrations.RenameField(
            model_name='resumen',
            old_name='Estudiante',
            new_name='estudiante',
        ),
        migrations.RenameField(
            model_name='voluntariado',
            old_name='Estudiante',
            new_name='estudiante',
        ),
    ]
