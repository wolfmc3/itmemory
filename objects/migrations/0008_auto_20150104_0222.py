# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('objects', '0007_auto_20150104_0218'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hardwareobject',
            options={'ordering': ['worksite'], 'verbose_name': 'Dispositivo hardware',
                     'verbose_name_plural': 'Dispositivi hardware'},
        ),
        migrations.AlterModelOptions(
            name='settinggroup',
            options={'ordering': ['name'], 'verbose_name': 'Gruppo impostazioni',
                     'verbose_name_plural': 'Gruppi impostazioni'},
        ),
        migrations.AlterModelOptions(
            name='settingstype',
            options={'ordering': ['group'], 'verbose_name': 'Tipo impostazione',
                     'verbose_name_plural': 'Tipi impostazione'},
        ),
    ]
