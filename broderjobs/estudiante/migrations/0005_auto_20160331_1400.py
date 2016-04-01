# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0004_auto_20160311_0925'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='foto_facebook',
            field=models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')]),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='semestre_actual',
            field=models.CharField(default=None, max_length=2, null=True, blank=True, choices=[(b'1', b'Ciclo 1'), (b'2', b'Ciclo 2'), (b'3', b'Ciclo 3'), (b'4', b'Ciclo 4'), (b'5', b'Ciclo 5'), (b'6', b'Ciclo 6'), (b'7', b'Ciclo 7'), (b'8', b'Ciclo 8'), (b'9', b'Ciclo 9'), (b'10', b'Ciclo 10')]),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='semestre_graduacion',
            field=models.CharField(default=None, max_length=2, null=True, blank=True, choices=[(b'1', b'Ciclo 1'), (b'2', b'Ciclo 2')]),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='semestre_inicio_estudio',
            field=models.CharField(default=None, max_length=2, null=True, blank=True, choices=[(b'1', b'Ciclo 1'), (b'2', b'Ciclo 2')]),
        ),
    ]
