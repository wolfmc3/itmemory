# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('objects', '0009_auto_20141227_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='hardwareobject',
            field=models.ForeignKey(to='objects.HardwareObject'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='settings',
            name='type',
            field=models.ForeignKey(related_name='settingstype', to='objects.SettingsType'),
            preserve_default=True,
        ),
    ]
