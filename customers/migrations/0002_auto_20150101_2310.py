# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'Cliente', 'verbose_name_plural': 'Clienti'},
        ),
        migrations.AlterModelOptions(
            name='worksite',
            options={'verbose_name': 'Sede', 'verbose_name_plural': 'Sedi'},
        ),
    ]
