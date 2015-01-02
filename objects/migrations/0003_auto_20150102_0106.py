# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('objects', '0002_auto_20150101_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='hardwareobject',
            field=models.ForeignKey(related_name='settings', verbose_name=b'Oggetto', to='objects.HardwareObject'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='settings',
            name='type',
            field=models.ForeignKey(related_name='settings', verbose_name=b'Tipo impostazione',
                                    to='objects.SettingsType'),
            preserve_default=True,
        ),
    ]
