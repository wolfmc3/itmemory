# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0011_hardwareobject_remote_token'),
        ('hpilo', '0008_ilonotifysetting'),
    ]

    operations = [
        migrations.AddField(
            model_name='ilonotifysetting',
            name='hardwareobject',
            field=models.ForeignKey(verbose_name=b'Server', blank=True, to='objects.HardwareObject', null=True),
            preserve_default=True,
        ),
    ]
