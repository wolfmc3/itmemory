# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('objects', '0012_auto_20141228_2357'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoftwarePassword',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField()),
                ('username', models.CharField(max_length=100, null=True, blank=True)),
                ('passwd', models.CharField(max_length=250, null=True, blank=True)),
                ('hardwareobject', models.ForeignKey(verbose_name=b'Oggetto', to='objects.HardwareObject')),
                ('settingtype', models.ForeignKey(related_name='softwarepasswords', verbose_name=b'Tipo impostazione',
                                                  to='objects.SettingsType')),
            ],
            options={
                'verbose_name': 'Password',
                'verbose_name_plural': 'Passwords',
            },
            bases=(models.Model,),
        ),
    ]
