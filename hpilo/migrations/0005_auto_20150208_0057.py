# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hpilo', '0004_auto_20150208_0054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ilostatusdetail',
            name='caution',
        ),
        migrations.RemoveField(
            model_name='ilostatusdetail',
            name='critical',
        ),
    ]
