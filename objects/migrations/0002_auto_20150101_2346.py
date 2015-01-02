# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('ittasks', '0001_initial'),
        ('objects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='settinggroup',
            name='activatetask',
            field=models.ForeignKey(verbose_name=b'Task da attivare', blank=True, to='ittasks.TaskTemplate', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='settingstype',
            name='activatetask',
            field=models.ForeignKey(verbose_name=b'Task da attivare', blank=True, to='ittasks.TaskTemplate', null=True),
            preserve_default=True,
        ),
    ]
