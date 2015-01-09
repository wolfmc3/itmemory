# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0009_hardwareobject_parentobject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hardwareobject',
            name='parentobject',
            field=models.ForeignKey(verbose_name=b'Dipende da:', blank=True, to='objects.HardwareObject', null=True),
            preserve_default=True,
        ),
    ]
