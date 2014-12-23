# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('ittasks', '0007_auto_20141223_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='laststart',
            field=models.DateTimeField(default=b'2013-01-01 00:00'),
            preserve_default=True,
        ),
    ]
