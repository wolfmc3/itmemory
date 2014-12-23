# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('ittasks', '0006_task_done'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='laststart',
            field=models.DateTimeField(default=b'2013-01-01'),
            preserve_default=True,
        ),
    ]
