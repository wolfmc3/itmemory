# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0010_auto_20150109_1232'),
    ]

    operations = [
        migrations.CreateModel(
            name='HwLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.TextField(verbose_name=b'Messaggio')),
                ('event_id', models.IntegerField(verbose_name=b'Id evento')),
                ('level', models.CharField(max_length=10, verbose_name=b'Livello')),
                ('record_id', models.IntegerField(verbose_name=b'Id record')),
                ('log_name', models.CharField(max_length=255, verbose_name=b'Nome log')),
                ('time', models.DateTimeField(verbose_name=b'Ora')),
                ('hardwareobject', models.ForeignKey(related_name='systemlogs', to='objects.HardwareObject')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
