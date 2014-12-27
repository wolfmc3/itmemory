# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('ittasks', '0010_auto_20141226_0321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskcheck',
            name='checktemplate',
            field=models.ForeignKey(related_name='checktemplates', blank=True, to='ittasks.TaskCheckTemplate'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='taskcheck',
            name='task',
            field=models.ForeignKey(related_name='tasks', blank=True, to='ittasks.Task'),
            preserve_default=True,
        ),
    ]
