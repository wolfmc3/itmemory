# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hpilo', '0002_auto_20150204_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='ilostatus',
            name='source',
            field=models.CharField(default=b'', max_length=255, null=True, verbose_name=b'Sorgente', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ilostatusdetail',
            name='caution',
            field=models.IntegerField(default=0, null=True, verbose_name=b'Minimo', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ilostatusdetail',
            name='critical',
            field=models.IntegerField(default=0, null=True, verbose_name=b'Massimo', blank=True),
            preserve_default=True,
        ),
    ]
