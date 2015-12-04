# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0021_auto_20151116_2347'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividadesextra',
            name='estado',
            field=models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')]),
        ),
        migrations.AddField(
            model_name='actividadesextra',
            name='fecha_creacion',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='actividadesextra',
            name='fecha_modificacion',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='estado',
            field=models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')]),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='fecha_creacion',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='fecha_modificacion',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='experienciaprofesional',
            name='estado',
            field=models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')]),
        ),
        migrations.AddField(
            model_name='experienciaprofesional',
            name='fecha_creacion',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='experienciaprofesional',
            name='fecha_modificacion',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='resumen',
            name='estado',
            field=models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')]),
        ),
        migrations.AddField(
            model_name='resumen',
            name='fecha_creacion',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='resumen',
            name='fecha_modificacion',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='voluntariado',
            name='estado',
            field=models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')]),
        ),
        migrations.AddField(
            model_name='voluntariado',
            name='fecha_creacion',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='voluntariado',
            name='fecha_modificacion',
            field=models.DateField(default=None, null=True, blank=True),
        ),
    ]
