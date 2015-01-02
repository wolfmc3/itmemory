# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=255)),
                ('address', models.TextField(max_length=500, null=True, verbose_name=b'Indirizzo', blank=True)),
                ('city', models.CharField(max_length=200, null=True, verbose_name=b'Citt\xc3\xa0', blank=True)),
                ('origin_code', models.CharField(max_length=25, null=True, verbose_name=b'Codice cliente', blank=True)),
                ('email', models.EmailField(max_length=255, null=True, verbose_name=b'Indirizzo email', blank=True)),
                ('telephone',
                 models.CharField(default=b'', max_length=255, null=True, verbose_name=b'Telefono', blank=True)),
                ('reference_person',
                 models.CharField(max_length=255, null=True, verbose_name=b'Persona di riferimento', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WorkSite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=255)),
                ('address', models.TextField(max_length=500, null=True, verbose_name=b'Indirizzo', blank=True)),
                ('city', models.CharField(max_length=200, null=True, verbose_name=b'Citt\xc3\xa0', blank=True)),
                ('origin_code', models.CharField(max_length=25, null=True, verbose_name=b'Codice cliente', blank=True)),
                ('email', models.EmailField(max_length=255, null=True, verbose_name=b'Indirizzo email', blank=True)),
                ('telephone',
                 models.CharField(default=b'', max_length=255, null=True, verbose_name=b'Telefono', blank=True)),
                ('reference_person',
                 models.CharField(max_length=255, null=True, verbose_name=b'Persona di riferimento', blank=True)),
                ('customer', models.ForeignKey(related_name='Worksites', to='customers.Customer')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
