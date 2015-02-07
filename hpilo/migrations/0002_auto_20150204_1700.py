# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import hpilo.models


class Migration(migrations.Migration):

    dependencies = [
        ('hpilo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ilostatusdetail',
            name='name',
            field=models.CharField(default=b'', max_length=255, null=True, verbose_name=b'Nome', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ilostatusdetail',
            name='status',
            field=hpilo.models.StatusCharField(max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ilostatusdetail',
            name='um',
            field=models.CharField(default=b'', max_length=255, null=True, verbose_name=b'Unita'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ilostatusdetail',
            name='component',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Componente', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ilostatusdetail',
            name='ilostatus',
            field=models.ForeignKey(related_name='statusdetails', to='hpilo.IloStatus'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ilostatusdetail',
            name='value',
            field=models.IntegerField(default=0, null=True, verbose_name=b'Valore', blank=True),
            preserve_default=True,
        ),
    ]
