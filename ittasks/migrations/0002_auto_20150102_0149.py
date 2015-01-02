# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('ittasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='hardwareobject',
            field=models.ForeignKey(related_name='tasks', verbose_name=b'Hardware associato',
                                    to='objects.HardwareObject'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='template',
            field=models.ForeignKey(related_name='tasks', verbose_name=b'Modello di task', to='ittasks.TaskTemplate'),
            preserve_default=True,
        ),
    ]
