# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('ittasks', '0008_auto_20141223_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='laststart',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
    ]
