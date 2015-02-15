# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hpilo', '0011_auto_20150214_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='ilostatus',
            name='history',
            field=models.BooleanField(default=False, verbose_name=b'Stato storico'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ilonotifysetting',
            name='type',
            field=models.CharField(default=b'exclude/status', max_length=255, verbose_name=b'Tipo', choices=[(b'exclude/status', b'Stato diverso da'), (b'filter/status', b'Stato uguale a')]),
            preserve_default=True,
        ),
    ]
