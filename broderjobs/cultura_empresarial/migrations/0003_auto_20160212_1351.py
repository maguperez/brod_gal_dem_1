# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cultura_empresarial', '0002_auto_20160212_1043'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Perfil_Cultura',
            new_name='PerfilCultura',
        ),
    ]
