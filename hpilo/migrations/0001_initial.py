# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import hpilo.models


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0011_hardwareobject_remote_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='IloStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', hpilo.models.StatusCharField(max_length=20)),
                ('bios', hpilo.models.StatusCharField(max_length=20)),
                ('fans', hpilo.models.StatusCharField(max_length=20)),
                ('memory', hpilo.models.StatusCharField(max_length=20)),
                ('network', hpilo.models.StatusCharField(max_length=20)),
                ('power', hpilo.models.StatusCharField(max_length=20)),
                ('processor', hpilo.models.StatusCharField(max_length=20)),
                ('storage', hpilo.models.StatusCharField(max_length=20)),
                ('temperature', hpilo.models.StatusCharField(max_length=20)),
                ('time', models.DateTimeField(verbose_name=b'Rilevamento')),
                ('hardwareobject', models.ForeignKey(related_name='ilostatuses', to='objects.HardwareObject')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IloStatusDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', models.CharField(max_length=255, verbose_name=b'Oggetto')),
                ('component', models.CharField(max_length=255, verbose_name=b'Componente')),
                ('value', models.CharField(max_length=255, verbose_name=b'Valore')),
                ('ilostatus', models.ForeignKey(related_name='statusdetail', to='hpilo.IloStatus')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
