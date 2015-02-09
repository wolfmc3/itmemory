# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hpilo', '0006_auto_20150208_0200'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ilostatus',
            options={'ordering': ['-time'], 'verbose_name': 'Stato HP Ilo', 'verbose_name_plural': 'Stati HP Ilo'},
        ),
        migrations.AlterModelOptions(
            name='ilostatusdetail',
            options={'ordering': ['item', 'component'], 'verbose_name': 'Dettaglio Stato HP Ilo', 'verbose_name_plural': 'Dettagli Stato HP Ilo'},
        ),
    ]
