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
                ('address', models.TextField(max_length=500)),
                ('city', models.CharField(max_length=200)),
                ('origin_code', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=255)),
                ('reference_person', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WorkSite',
            fields=[
                ('customer_ptr',
                 models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False,
                                      to='customers.Customer')),
                ('customer', models.ForeignKey(related_name='Worksites', to='customers.Customer')),
            ],
            options={
            },
            bases=('customers.customer',),
        ),
    ]
