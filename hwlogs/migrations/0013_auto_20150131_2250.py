# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hwlogs', '0012_auto_20150131_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logfilter',
            name='name',
            field=models.CharField(max_length=125, verbose_name=b'Nome/Oggetto'),
            preserve_default=True,
        ),
    ]
