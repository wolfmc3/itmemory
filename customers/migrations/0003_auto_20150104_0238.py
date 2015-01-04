# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('customers', '0002_auto_20150101_2310'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['name'], 'verbose_name': 'Cliente', 'verbose_name_plural': 'Clienti'},
        ),
        migrations.AlterModelOptions(
            name='worksite',
            options={'ordering': ['name'], 'verbose_name': 'Sede', 'verbose_name_plural': 'Sedi'},
        ),
    ]
