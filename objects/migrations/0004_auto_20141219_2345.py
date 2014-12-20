# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('objects', '0003_auto_20141217_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='type',
            field=models.ForeignKey(related_name='settingstype', to='objects.SettingsType'),
            preserve_default=True,
        ),
    ]
