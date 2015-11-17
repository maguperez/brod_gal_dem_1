# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_beneficio_tiporemuneracion'),
        ('empresa', '0007_auto_20151116_1328'),
        ('oportunidad', '0002_auto_20151115_2159'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerfilCandidato',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('carrera', models.ManyToManyField(default=None, to='main.Carrera', verbose_name=b'carrera', blank=True)),
                ('ciudad', models.ForeignKey(default=None, blank=True, to='main.Ciudad', null=True)),
                ('grado_estudio', models.ForeignKey(default=None, blank=True, to='main.GradoEstudio', null=True)),
                ('idioma', models.ManyToManyField(default=None, to='main.Idioma', verbose_name=b'Idioma', blank=True)),
                ('pais', models.ForeignKey(default=None, blank=True, to='main.Pais', null=True)),
                ('universidad', models.ManyToManyField(default=None, to='main.Universidad', verbose_name=b'universidad', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='empresa',
            field=models.ForeignKey(default=None, blank=True, to='empresa.Empresa', null=True),
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='resumen',
            field=models.CharField(default=None, max_length=b'1000', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='perfil_candidato',
            field=models.ForeignKey(default=None, blank=True, to='oportunidad.PerfilCandidato', null=True),
        ),
    ]
