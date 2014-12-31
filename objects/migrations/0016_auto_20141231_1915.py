# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('objects', '0015_softwarepassword_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='softwarepassword',
            name='hardwareobject',
            field=models.ForeignKey(related_name='softwarepasswords', verbose_name=b'Oggetto',
                                    to='objects.HardwareObject'),
            preserve_default=True,
        ),
    ]
