# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0002_auto_20160303_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='semestre_actual',
            field=models.CharField(default=None, max_length=2, null=True, blank=True, choices=[(b'', b'Ciclo'), (b'1', b'Ciclo 1'), (b'2', b'Ciclo 2'), (b'3', b'Ciclo 3'), (b'4', b'Ciclo 4'), (b'5', b'Ciclo 5'), (b'6', b'Ciclo 6'), (b'7', b'Ciclo 7'), (b'8', b'Ciclo 8'), (b'9', b'Ciclo 9'), (b'10', b'Ciclo 10')]),
        ),
    ]
