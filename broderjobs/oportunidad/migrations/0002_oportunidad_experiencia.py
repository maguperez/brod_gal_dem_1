# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oportunidad', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='oportunidad',
            name='experiencia',
            field=models.CharField(default=None, max_length=b'1', null=True, blank=True, choices=[(b'', b'A\xc3\xb1o'), (b'0', b'sin experiencia'), (b'1', b'hasta 1 a\xc3\xb1o'), (b'2', b'desde 2a\xc3\xb1os'), (b'3', b'desde 3a\xc3\xb1os'), (b'4', b'desde 4a\xc3\xb1os'), (b'5', b'desde 5a\xc3\xb1os'), (b'6', b'desde 6a\xc3\xb1os'), (b'7', b'desde 7a\xc3\xb1os'), (b'8', b'desde 8a\xc3\xb1os'), (b'9', b'desde 9a\xc3\xb1os'), (b'10', b'desde 10a\xc3\xb1os')]),
        ),
    ]
