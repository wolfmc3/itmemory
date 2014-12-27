# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('objects', '0007_auto_20141227_0240'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hardwareobject',
            options={'verbose_name': 'Dispositivo hardware', 'verbose_name_plural': 'Dispositivi hardware'},
        ),
    ]
