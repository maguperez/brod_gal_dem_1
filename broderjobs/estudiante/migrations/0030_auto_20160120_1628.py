# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0029_auto_20160106_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='semestre_graduacion',
            field=models.CharField(default=None, max_length=2, null=True, blank=True, choices=[(b'', b'Semestre'), (b'1', b'Ciclo 1'), (b'2', b'Ciclo 2')]),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='semestre_inicio_estudio',
            field=models.CharField(default=None, max_length=2, null=True, blank=True, choices=[(b'', b'Semestre'), (b'1', b'Ciclo 1'), (b'2', b'Ciclo 2')]),
        ),
    ]
