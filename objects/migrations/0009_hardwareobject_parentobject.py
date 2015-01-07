# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0008_auto_20150104_0222'),
    ]

    operations = [
        migrations.AddField(
            model_name='hardwareobject',
            name='parentobject',
            field=models.ForeignKey(blank=True, to='objects.HardwareObject', null=True),
            preserve_default=True,
        ),
    ]
