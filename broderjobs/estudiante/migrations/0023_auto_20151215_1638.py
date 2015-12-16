# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0022_auto_20151203_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='experienciaprofesional',
            name='empresa_referancial',
            field=models.CharField(default=None, max_length=b'50', null=True),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='semestre_graduacion',
            field=models.CharField(default=None, max_length=2, null=True, blank=True, choices=[(b'', b'Semestre'), (b'0', b'Sem 0'), (b'1', b'Sem 1'), (b'2', b'Sem 2')]),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='semestre_inicio_estudio',
            field=models.CharField(default=None, max_length=2, null=True, blank=True, choices=[(b'', b'Semestre'), (b'0', b'Sem 0'), (b'1', b'Sem 1'), (b'2', b'Sem 2')]),
        ),
    ]
