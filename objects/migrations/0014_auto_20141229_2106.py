# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('objects', '0013_softwarepassword'),
    ]

    operations = [
        migrations.AlterField(
            model_name='softwarepassword',
            name='passwd',
            field=models.BinaryField(max_length=250, null=True, blank=True),
            preserve_default=True,
        ),
    ]
