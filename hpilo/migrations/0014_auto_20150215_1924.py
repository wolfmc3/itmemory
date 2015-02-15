# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hpilo', '0013_auto_20150215_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ilonotifysetting',
            name='type',
            field=models.CharField(default=b'exclude/*', max_length=255, verbose_name=b'Tipo', choices=[(b'exclude/*', b'Stato sensori diverso da'), (b'filter/*', b'Stato sensori uguale a')]),
            preserve_default=True,
        ),
    ]
