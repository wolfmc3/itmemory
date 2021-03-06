# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hpilo', '0012_auto_20150214_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ilonotifysetting',
            name='type',
            field=models.CharField(default=b'exclude/status', max_length=255, verbose_name=b'Tipo', choices=[(b'exclude/status__exact', b'Stato diverso da'), (b'filter/status__exact', b'Stato uguale a')]),
            preserve_default=True,
        ),
    ]
