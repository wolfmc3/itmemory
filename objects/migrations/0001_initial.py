# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HardwareObject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('item', models.CharField(max_length=32)),
                ('serial', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=250)),
                ('worksite', models.ForeignKey(related_name='objects', to='customers.WorkSite')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
