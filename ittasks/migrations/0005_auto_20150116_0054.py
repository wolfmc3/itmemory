# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('ittasks', '0004_auto_20150115_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasktemplate',
            name='send_expiration_group',
            field=models.ForeignKey(related_name='template_exp_to_notify', verbose_name=b'Gruppo notifiche scadenze', blank=True, to='auth.Group', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tasktemplate',
            name='send_reminder_group',
            field=models.ForeignKey(related_name='template_to_notify', verbose_name=b'Gruppo notifiche', blank=True, to='auth.Group', null=True),
            preserve_default=True,
        ),
    ]
