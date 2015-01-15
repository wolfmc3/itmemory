# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ittasks', '0003_auto_20150109_0944'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='expired_send_date',
            field=models.DateTimeField(null=True, verbose_name=b'Ultimo invio scadenza', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='task',
            name='reminder_send_date',
            field=models.DateTimeField(null=True, verbose_name=b'Ultimo invio promemoria', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tasktemplate',
            name='send_expiration',
            field=models.BooleanField(default=True, verbose_name=b'Invia promemoria scadenza'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tasktemplate',
            name='send_reminder',
            field=models.BooleanField(default=True, verbose_name=b'Invia promemoria'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='user',
            field=models.ForeignKey(related_name='assigned_tasks', verbose_name=b'Utente assegnato', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
