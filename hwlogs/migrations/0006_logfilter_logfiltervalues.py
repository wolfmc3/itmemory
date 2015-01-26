# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hwlogs', '0005_auto_20150125_0111'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogFilter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25, verbose_name=b'Nome')),
                ('operation', models.IntegerField(verbose_name=b'Operazione', choices=[(1, b'Non importa, cancella'), (2, b'Notifica via email'), (3, b'Segna come importante')])),
                ('user', models.ForeignKey(related_name='logfilters', verbose_name=b'Destinatario mail', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LogFilterValues',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value_field', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
