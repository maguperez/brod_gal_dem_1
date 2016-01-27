# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disc', '0006_disccodificacion_valor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='disccodificacion',
            options={'ordering': ['segmento', 'letra', 'orden']},
        ),
    ]
