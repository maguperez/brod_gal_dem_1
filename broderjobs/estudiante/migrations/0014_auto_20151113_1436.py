# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0013_auto_20151113_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='ano_graduacion',
            field=models.CharField(default=None, max_length=4, null=True, blank=True, choices=[(b'', b'A\xc3\xb1os'), (b'1980', b'1980'), (b'1981', b'1981'), (b'1982', b'1982'), (b'1983', b'1983'), (b'1984', b'1984'), (b'1985', b'1985'), (b'1986', b'1986'), (b'1987', b'1987'), (b'1988', b'1988'), (b'1989', b'1989'), (b'1990', b'1990'), (b'1991', b'1991'), (b'1992', b'1992'), (b'1993', b'1993'), (b'1994', b'1994'), (b'1995', b'1995'), (b'1996', b'1996'), (b'1997', b'1997'), (b'1998', b'1998'), (b'1999', b'1999'), (b'2000', b'2000'), (b'2001', b'2001'), (b'2002', b'2002'), (b'2003', b'2003'), (b'2004', b'2004'), (b'2005', b'2005'), (b'2006', b'2006'), (b'2007', b'2007'), (b'2008', b'2008'), (b'2009', b'2009'), (b'2010', b'2010'), (b'2011', b'2011'), (b'2012', b'2012'), (b'2013', b'2013'), (b'2014', b'2014'), (b'2015', b'2015'), (b'2016', b'2016'), (b'2017', b'2017'), (b'2018', b'2018'), (b'2019', b'2019')]),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='ano_inicio_estudio',
            field=models.CharField(default=None, max_length=4, null=True, blank=True, choices=[(b'', b'A\xc3\xb1os'), (b'1980', b'1980'), (b'1981', b'1981'), (b'1982', b'1982'), (b'1983', b'1983'), (b'1984', b'1984'), (b'1985', b'1985'), (b'1986', b'1986'), (b'1987', b'1987'), (b'1988', b'1988'), (b'1989', b'1989'), (b'1990', b'1990'), (b'1991', b'1991'), (b'1992', b'1992'), (b'1993', b'1993'), (b'1994', b'1994'), (b'1995', b'1995'), (b'1996', b'1996'), (b'1997', b'1997'), (b'1998', b'1998'), (b'1999', b'1999'), (b'2000', b'2000'), (b'2001', b'2001'), (b'2002', b'2002'), (b'2003', b'2003'), (b'2004', b'2004'), (b'2005', b'2005'), (b'2006', b'2006'), (b'2007', b'2007'), (b'2008', b'2008'), (b'2009', b'2009'), (b'2010', b'2010'), (b'2011', b'2011'), (b'2012', b'2012'), (b'2013', b'2013'), (b'2014', b'2014'), (b'2015', b'2015'), (b'2016', b'2016'), (b'2017', b'2017'), (b'2018', b'2018'), (b'2019', b'2019')]),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='semestre_graduacion',
            field=models.CharField(default=None, max_length=2, null=True, blank=True, choices=[(b'', b'Semestre'), (b'0', b'0'), (b'1', b'1'), (b'2', b'2')]),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='semestre_inicio_estudio',
            field=models.CharField(default=None, max_length=2, null=True, blank=True, choices=[(b'', b'Semestre'), (b'0', b'0'), (b'1', b'1'), (b'2', b'2')]),
        ),
    ]
