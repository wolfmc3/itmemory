# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hwlogs', '0003_auto_20150124_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hwlog',
            name='level',
            field=models.CharField(max_length=10, verbose_name=b'Livello', choices=[(b'0', b'Emergency'), (b'1', b'Alert'), (b'2', b'Critical'), (b'3', b'Error'), (b'4', b'Warning'), (b'5', b'Notice'), (b'6', b'Informational'), (b'7', b'Debug')]),
            preserve_default=True,
        ),
    ]
