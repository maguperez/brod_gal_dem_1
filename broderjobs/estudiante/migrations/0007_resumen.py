# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0006_actividadesextra_experienciaprofesional_voluntariado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resumen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=b'100')),
                ('Estudiante', models.ForeignKey(to='estudiante.Estudiante')),
            ],
        ),
    ]
