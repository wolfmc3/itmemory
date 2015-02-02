# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hwlogs', '0011_auto_20150126_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='hwlog',
            name='important',
            field=models.BooleanField(default=False, verbose_name=b'Importante'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hwlog',
            name='notify_count',
            field=models.IntegerField(default=0, verbose_name=b'Notifiche inviate'),
            preserve_default=True,
        ),
    ]
