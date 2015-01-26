# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hwlogs', '0006_logfilter_logfiltervalues'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logfiltervalues',
            name='value_field',
            field=models.CharField(max_length=255, choices=[(b'level', b'Livello')]),
            preserve_default=True,
        ),
    ]
