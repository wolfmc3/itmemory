# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hwlogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hwlog',
            name='record_id',
            field=models.IntegerField(null=True, verbose_name=b'Id record', blank=True),
            preserve_default=True,
        ),
    ]
