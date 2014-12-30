# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('objects', '0014_auto_20141229_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='softwarepassword',
            name='password',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
    ]
