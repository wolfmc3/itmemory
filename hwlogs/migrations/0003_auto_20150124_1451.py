# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hwlogs', '0002_auto_20150124_0415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hwlog',
            name='level',
            field=models.CharField(max_length=10, verbose_name=b'Livello', choices=[(0, b'Emergency'), (1, b'Alert'), (2, b'Critical'), (3, b'Error'), (4, b'Warning'), (5, b'Notice'), (6, b'Informational'), (7, b'Debug')]),
            preserve_default=True,
        ),
    ]
