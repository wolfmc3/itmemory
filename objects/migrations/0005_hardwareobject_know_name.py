# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('objects', '0004_auto_20141219_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='hardwareobject',
            name='know_name',
            field=models.CharField(default=b'', max_length=255),
            preserve_default=True,
        ),
    ]
