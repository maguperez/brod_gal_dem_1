# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_beneficio_tiporemuneracion'),
        ('oportunidad', '0006_auto_20151117_0917'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerfilOportunidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('carrera', models.ManyToManyField(default=None, to='main.Carrera', verbose_name=b'carrera', blank=True)),
                ('ciudad', models.ForeignKey(default=None, blank=True, to='main.Ciudad', null=True)),
                ('conocimiento', models.ManyToManyField(default=None, to='main.Conocimiento', verbose_name=b'Conocimiento', blank=True)),
                ('grado_estudio', models.ForeignKey(default=None, blank=True, to='main.GradoEstudio', null=True)),
                ('idioma', models.ManyToManyField(default=None, to='main.Idioma', verbose_name=b'Idioma', blank=True)),
                ('pais', models.ForeignKey(default=None, blank=True, to='main.Pais', null=True)),
                ('universidad', models.ManyToManyField(default=None, to='main.Universidad', verbose_name=b'universidad', blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='perfilcandidato',
            name='carrera',
        ),
        migrations.RemoveField(
            model_name='perfilcandidato',
            name='ciudad',
        ),
        migrations.RemoveField(
            model_name='perfilcandidato',
            name='conocimiento',
        ),
        migrations.RemoveField(
            model_name='perfilcandidato',
            name='grado_estudio',
        ),
        migrations.RemoveField(
            model_name='perfilcandidato',
            name='idioma',
        ),
        migrations.RemoveField(
            model_name='perfilcandidato',
            name='pais',
        ),
        migrations.RemoveField(
            model_name='perfilcandidato',
            name='universidad',
        ),
        migrations.RemoveField(
            model_name='oportunidad',
            name='perfil_candidato',
        ),
        migrations.AlterField(
            model_name='oportunidad',
            name='beneficio',
            field=models.ForeignKey(verbose_name=b'Beneficio', blank=True, to='main.Beneficio', null=True),
        ),
        migrations.AlterField(
            model_name='oportunidad',
            name='carga_horaria',
            field=models.ForeignKey(verbose_name=b'Jornada Laboral', blank=True, to='main.CargaHoraria', null=True),
        ),
        migrations.AlterField(
            model_name='oportunidad',
            name='remuneracion',
            field=models.ForeignKey(verbose_name=b'Remuneracion', blank=True, to='main.TipoRemuneracion', null=True),
        ),
        migrations.AlterField(
            model_name='oportunidad',
            name='tipo_puesto',
            field=models.ForeignKey(verbose_name=b'Tipo Puesto', blank=True, to='main.TipoPuesto', null=True),
        ),
        migrations.DeleteModel(
            name='PerfilCandidato',
        ),
        migrations.AddField(
            model_name='oportunidad',
            name='perfil_oportunidad',
            field=models.ForeignKey(default=None, blank=True, to='oportunidad.PerfilOportunidad', null=True),
        ),
    ]
