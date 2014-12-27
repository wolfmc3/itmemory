# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('objects', '0010_auto_20141227_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='hardwareobject',
            field=models.ForeignKey(verbose_name=b'Oggetto', to='objects.HardwareObject'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='settings',
            name='type',
            field=models.ForeignKey(related_name='settingstype', verbose_name=b'Tipo impostazione',
                                    to='objects.SettingsType'),
            preserve_default=True,
        ),
    ]
