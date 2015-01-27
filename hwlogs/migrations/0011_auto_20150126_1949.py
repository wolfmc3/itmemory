# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hwlogs', '0010_auto_20150126_1455'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='logfiltervalues',
            options={'ordering': ['weight'], 'verbose_name': 'Valore di filtro', 'verbose_name_plural': 'Valori di filtro'},
        ),
        migrations.AddField(
            model_name='logfiltervalues',
            name='exclude_value',
            field=models.IntegerField(default=0, verbose_name=b'Escludi valori', choices=[(0, b'Includi'), (1, b'Escludi')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='logfiltervalues',
            name='weight',
            field=models.IntegerField(default=1, verbose_name=b'Ordine'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='logfilter',
            name='operation',
            field=models.IntegerField(verbose_name=b'Operazione', choices=[(0, b'Visualizza'), (1, b'Non importare, cancella'), (2, b'Notifica via email'), (3, b'Segna come importante')]),
            preserve_default=True,
        ),
    ]
