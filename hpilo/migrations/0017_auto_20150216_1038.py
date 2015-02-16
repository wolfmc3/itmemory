# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hpilo', '0016_auto_20150215_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='ilostatus',
            name='notified',
            field=models.BooleanField(default=False, verbose_name=b'Notificato'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ilonotifysetting',
            name='type',
            field=models.CharField(default=b'exclude/*', max_length=255, verbose_name=b'Tipo', choices=[(b'exclude/*__contains', b'Stato sensori diverso da'), (b'filter/*__contains', b'Stato sensori uguale a'), (b'exclude/temperature__contains', b'Stato sensore TEMP diverso da'), (b'exclude/storage__contains', b'Stato sensore dischi diverso da'), (b'filter/source__contains', b'Sorgente contiene')]),
            preserve_default=True,
        ),
    ]
