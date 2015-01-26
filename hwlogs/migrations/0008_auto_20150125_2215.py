# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hwlogs', '0007_auto_20150125_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='logfiltervalues',
            name='logfilter',
            field=models.ForeignKey(related_name='filters', default=None, verbose_name=b'Filtro', to='hwlogs.LogFilter'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logfiltervalues',
            name='operation',
            field=models.IntegerField(default=0, verbose_name=b'Confronto', choices=[(0, b'uguale'), (1, b'diverso'), (2, b'contiene'), (3, b'maggiore di'), (4, b'minore di'), (5, b'uguale o maggiore di'), (6, b'uguale o minore di')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logfiltervalues',
            name='value',
            field=models.TextField(default='', verbose_name=b'Valore'),
            preserve_default=False,
        ),
    ]
