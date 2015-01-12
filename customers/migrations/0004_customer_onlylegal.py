# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_auto_20150104_0238'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='onlylegal',
            field=models.BooleanField(default=False, verbose_name=b'Solo sede legale'),
            preserve_default=True,
        ),
    ]
