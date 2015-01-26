# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('hwlogs', '0008_auto_20150125_2215'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='logfilter',
            options={'ordering': ['-name'], 'verbose_name': 'Filtro log', 'verbose_name_plural': 'Filtri log'},
        ),
        migrations.AlterModelOptions(
            name='logfiltervalues',
            options={'verbose_name': 'Valore di filtro', 'verbose_name_plural': 'Valori di filtro'},
        ),
        migrations.AddField(
            model_name='logfilter',
            name='group',
            field=models.ForeignKey(related_name='logfilters', verbose_name=b'Destinatari mail', blank=True, to='auth.Group', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='logfilter',
            name='operation',
            field=models.IntegerField(verbose_name=b'Operazione', choices=[(0, b'Visualizza'), (1, b'Non importa, cancella'), (2, b'Notifica via email'), (3, b'Segna come importante')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='logfiltervalues',
            name='operation',
            field=models.IntegerField(verbose_name=b'Confronto', choices=[(0, b'uguale'), (1, b'contiene'), (2, b'maggiore di'), (3, b'minore di'), (4, b'uguale o maggiore di'), (5, b'uguale o minore di')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='logfiltervalues',
            name='value_field',
            field=models.CharField(max_length=255, choices=[(b'event_id', b'Id evento'), (b'level', b'Livello'), (b'log_name', b'Nome log'), (b'message', b'Messaggio'), (b'record_id', b'Id record'), (b'time', b'Ora')]),
            preserve_default=True,
        ),
    ]
