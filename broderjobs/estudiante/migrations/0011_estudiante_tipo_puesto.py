# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_conocimiento'),
        ('estudiante', '0010_estudianteconocimiento_estudianteidioma'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='tipo_puesto',
            field=models.ManyToManyField(to='main.TipoPuesto', null=True, verbose_name=b'Tipo Puesto', blank=True),
        ),
    ]
