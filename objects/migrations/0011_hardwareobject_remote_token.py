# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import objects.models


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0010_auto_20150109_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='hardwareobject',
            name='remote_token',
            field=models.CharField(default=objects.models.newToken, max_length=32),
            preserve_default=True,
        ),
    ]
