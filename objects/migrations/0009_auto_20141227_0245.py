# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('objects', '0008_auto_20141227_0241'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='settinggroup',
            options={'verbose_name': 'Gruppo impostazioni', 'verbose_name_plural': 'Gruppi impostazioni'},
        ),
        migrations.AlterModelOptions(
            name='settings',
            options={'verbose_name': 'Impostazione', 'verbose_name_plural': 'Impostazioni'},
        ),
        migrations.AlterModelOptions(
            name='settingstype',
            options={'verbose_name': 'Tipo impostazione', 'verbose_name_plural': 'Tipi impostazione'},
        ),
    ]
