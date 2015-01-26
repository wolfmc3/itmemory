# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hwlogs', '0009_auto_20150126_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hwlog',
            name='level',
            field=models.CharField(max_length=10, verbose_name=b'Livello', choices=[(b'0', b'Undefinited'), (b'1', b'Critical'), (b'2', b'Error'), (b'3', b'Warning'), (b'4', b'Informational'), (b'5', b'Verbose')]),
            preserve_default=True,
        ),
    ]
