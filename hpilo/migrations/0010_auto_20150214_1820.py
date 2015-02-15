# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hpilo', '0009_ilonotifysetting_hardwareobject'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='ilonotifysetting',
            unique_together=set([('type', 'search_value', 'hardwareobject')]),
        ),
    ]
