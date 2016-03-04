# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0001_initial'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActividadesExtra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.TextField(default=None, null=True, blank=True)),
                ('organizacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_creacion', models.DateField(default=datetime.datetime.now, null=True, blank=True)),
                ('fecha_modificacion', models.DateField(default=datetime.datetime.now, null=True, blank=True)),
                ('estado', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')])),
            ],
        ),
        migrations.CreateModel(
            name='ConocimientoExtra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('orden', models.IntegerField(null=True, blank=True)),
                ('fecha_creacion', models.DateField(default=datetime.datetime.now, null=True, blank=True)),
                ('fecha_modificacion', models.DateField(default=datetime.datetime.now, null=True, blank=True)),
                ('estado', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')])),
            ],
            options={
                'ordering': ['orden'],
            },
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('carrera_referencial', models.CharField(default=None, max_length=b'100', null=True, blank=True)),
                ('semestre_inicio_estudio', models.CharField(default=None, max_length=2, null=True, blank=True, choices=[(b'', b'Ciclo'), (b'1', b'Ciclo 1'), (b'2', b'Ciclo 2')])),
                ('ano_inicio_estudio', models.CharField(default=None, max_length=4, null=True, blank=True, choices=[(b'', b'A\xc3\xb1o'), (b'1980', b'1980'), (b'1981', b'1981'), (b'1982', b'1982'), (b'1983', b'1983'), (b'1984', b'1984'), (b'1985', b'1985'), (b'1986', b'1986'), (b'1987', b'1987'), (b'1988', b'1988'), (b'1989', b'1989'), (b'1990', b'1990'), (b'1991', b'1991'), (b'1992', b'1992'), (b'1993', b'1993'), (b'1994', b'1994'), (b'1995', b'1995'), (b'1996', b'1996'), (b'1997', b'1997'), (b'1998', b'1998'), (b'1999', b'1999'), (b'2000', b'2000'), (b'2001', b'2001'), (b'2002', b'2002'), (b'2003', b'2003'), (b'2004', b'2004'), (b'2005', b'2005'), (b'2006', b'2006'), (b'2007', b'2007'), (b'2008', b'2008'), (b'2009', b'2009'), (b'2010', b'2010'), (b'2011', b'2011'), (b'2012', b'2012'), (b'2013', b'2013'), (b'2014', b'2014'), (b'2015', b'2015'), (b'2016', b'2016'), (b'2017', b'2017'), (b'2018', b'2018'), (b'2019', b'2019')])),
                ('semestre_graduacion', models.CharField(default=None, max_length=2, null=True, blank=True, choices=[(b'', b'Ciclo'), (b'1', b'Ciclo 1'), (b'2', b'Ciclo 2')])),
                ('ano_graduacion', models.CharField(default=None, max_length=4, null=True, blank=True, choices=[(b'', b'A\xc3\xb1o'), (b'1980', b'1980'), (b'1981', b'1981'), (b'1982', b'1982'), (b'1983', b'1983'), (b'1984', b'1984'), (b'1985', b'1985'), (b'1986', b'1986'), (b'1987', b'1987'), (b'1988', b'1988'), (b'1989', b'1989'), (b'1990', b'1990'), (b'1991', b'1991'), (b'1992', b'1992'), (b'1993', b'1993'), (b'1994', b'1994'), (b'1995', b'1995'), (b'1996', b'1996'), (b'1997', b'1997'), (b'1998', b'1998'), (b'1999', b'1999'), (b'2000', b'2000'), (b'2001', b'2001'), (b'2002', b'2002'), (b'2003', b'2003'), (b'2004', b'2004'), (b'2005', b'2005'), (b'2006', b'2006'), (b'2007', b'2007'), (b'2008', b'2008'), (b'2009', b'2009'), (b'2010', b'2010'), (b'2011', b'2011'), (b'2012', b'2012'), (b'2013', b'2013'), (b'2014', b'2014'), (b'2015', b'2015'), (b'2016', b'2016'), (b'2017', b'2017'), (b'2018', b'2018'), (b'2019', b'2019')])),
                ('foto', models.ImageField(upload_to=b'img/%Y/%m/%d', null=True, verbose_name=b'foto perfil', blank=True)),
                ('completo_test', models.BooleanField(default=False)),
                ('fecha_creacion', models.DateField(default=datetime.datetime.now, null=True, blank=True)),
                ('fecha_modificacion', models.DateField(default=datetime.datetime.now, null=True, blank=True)),
                ('estado', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')])),
                ('carga_horaria', models.ForeignKey(default=None, blank=True, to='main.CargaHoraria', null=True)),
                ('carrera', models.ForeignKey(default=None, blank=True, to='main.Carrera', null=True)),
                ('ciudad', models.ForeignKey(default=None, blank=True, to='main.Ciudad', null=True)),
                ('conocimiento', models.ManyToManyField(default=None, to='main.Conocimiento', verbose_name=b'Conocimiento', blank=True)),
                ('grado_estudio', models.ForeignKey(default=None, blank=True, to='main.GradoEstudio', null=True)),
                ('idioma', models.ManyToManyField(default=None, to='main.Idioma', verbose_name=b'Idioma', blank=True)),
                ('pais', models.ForeignKey(default=None, blank=True, to='main.Pais', null=True)),
                ('persona', models.OneToOneField(to='main.Persona')),
                ('tipo_puesto', models.ManyToManyField(default=None, to='main.TipoPuesto', verbose_name=b'Tipo Puesto', blank=True)),
                ('universidad', models.ForeignKey(default=None, blank=True, to='main.Universidad', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExperienciaProfesional',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('puesto_referencial', models.CharField(default=None, max_length=b'50', null=True)),
                ('empresa_referencial', models.CharField(default=None, max_length=b'50', null=True)),
                ('fecha_desde', models.DateField(default=None, null=True, blank=True)),
                ('fecha_hasta', models.DateField(default=None, null=True, blank=True)),
                ('trabajo_actual', models.CharField(default=b'N', max_length=1)),
                ('descripcion', models.CharField(default=None, max_length=b'1000', null=True)),
                ('fecha_creacion', models.DateField(default=datetime.datetime.now, null=True, blank=True)),
                ('fecha_modificacion', models.DateField(default=datetime.datetime.now, null=True, blank=True)),
                ('estado', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')])),
                ('empresa', models.ForeignKey(default=None, blank=True, to='empresa.Empresa', null=True)),
                ('estudiante', models.ForeignKey(default=None, blank=True, to='estudiante.Estudiante', null=True)),
                ('puesto', models.ForeignKey(default=None, blank=True, to='empresa.Puesto', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resumen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(default=None, max_length=b'1000', null=True, blank=True)),
                ('fecha_creacion', models.DateField(default=datetime.datetime.now, null=True, blank=True)),
                ('fecha_modificacion', models.DateField(default=datetime.datetime.now, null=True, blank=True)),
                ('estado', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')])),
                ('estudiante', models.ForeignKey(to='estudiante.Estudiante')),
            ],
        ),
        migrations.CreateModel(
            name='Voluntariado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cargo', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('organizacion', models.CharField(default=None, max_length=b'50', null=True, blank=True)),
                ('fecha_desde', models.DateField(null=True)),
                ('fecha_hasta', models.DateField(default=None, null=True, blank=True)),
                ('voluntariado_actual', models.CharField(default=b'N', max_length=1)),
                ('descripcion', models.CharField(default=None, max_length=b'1000', null=True, blank=True)),
                ('fecha_creacion', models.DateField(default=datetime.datetime.now, null=True, blank=True)),
                ('fecha_modificacion', models.DateField(default=datetime.datetime.now, null=True, blank=True)),
                ('estado', models.CharField(default=b'A', max_length=1, null=True, blank=True, choices=[(b'A', b'Activo'), (b'I', b'Inactivado')])),
                ('estudiante', models.ForeignKey(default=None, blank=True, to='estudiante.Estudiante', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='conocimientoextra',
            name='estudiante',
            field=models.ForeignKey(default=None, blank=True, to='estudiante.Estudiante', null=True),
        ),
        migrations.AddField(
            model_name='actividadesextra',
            name='estudiante',
            field=models.ForeignKey(to='estudiante.Estudiante'),
        ),
    ]
