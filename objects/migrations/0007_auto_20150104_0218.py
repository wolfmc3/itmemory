# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('objects', '0006_auto_20150102_1310'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='settings',
            options={'ordering': ['type'], 'verbose_name': 'Impostazione', 'verbose_name_plural': 'Impostazioni'},
        ),
        migrations.AlterModelOptions(
            name='softwarepassword',
            options={'ordering': ['settingtype'], 'verbose_name': 'Password', 'verbose_name_plural': 'Passwords'},
        ),
    ]
