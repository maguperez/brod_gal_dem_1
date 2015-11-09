# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20151109_1012'),
        ('estudiante', '0002_auto_20151107_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='ciudad',
            field=models.ForeignKey(to='main.Ciudad', null=True),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='carerra',
            field=models.ForeignKey(to='main.Carrera', null=True),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='grado_estudio',
            field=models.ForeignKey(to='main.GradoEstudio', null=True),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='pais',
            field=models.ForeignKey(default=0, to='main.Pais'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='universidad',
            field=models.ForeignKey(to='main.Universidad', null=True),
        ),
    ]
