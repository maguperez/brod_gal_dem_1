# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disc', '0010_auto_20160128_1025'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='disccodificacion',
            options={'ordering': ['letra', 'valor_desde', 'valor_hasta', 'segmento', 'orden']},
        ),
        migrations.AddField(
            model_name='perfil',
            name='no_concluyente',
            field=models.BooleanField(default=False),
        ),
    ]
