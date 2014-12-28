# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('objects', '0011_auto_20141227_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hardwareobject',
            name='worksite',
            field=models.ForeignKey(related_name='hardwareobjects', verbose_name=b'Luogo di installazione',
                                    to='customers.WorkSite'),
            preserve_default=True,
        ),
    ]
