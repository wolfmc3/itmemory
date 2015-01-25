# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hwlogs', '0004_auto_20150124_1457'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hwlog',
            options={'ordering': ['-time'], 'verbose_name': 'Log dispositivo', 'verbose_name_plural': 'Logs dispositivo'},
        ),
    ]
