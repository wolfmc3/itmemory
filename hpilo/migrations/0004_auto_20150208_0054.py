# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hpilo', '0003_auto_20150208_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ilostatusdetail',
            name='caution',
            field=models.IntegerField(default=0, null=True, verbose_name=b'Attenzione', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ilostatusdetail',
            name='critical',
            field=models.IntegerField(default=0, null=True, verbose_name=b'Critico', blank=True),
            preserve_default=True,
        ),
    ]
