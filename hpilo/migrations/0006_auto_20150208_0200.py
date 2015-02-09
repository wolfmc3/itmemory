# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import hpilo.models


class Migration(migrations.Migration):

    dependencies = [
        ('hpilo', '0005_auto_20150208_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ilostatus',
            name='bios',
            field=hpilo.models.StatusCharField(max_length=125),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ilostatus',
            name='fans',
            field=hpilo.models.StatusCharField(max_length=125),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ilostatus',
            name='memory',
            field=hpilo.models.StatusCharField(max_length=125),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ilostatus',
            name='network',
            field=hpilo.models.StatusCharField(max_length=125),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ilostatus',
            name='power',
            field=hpilo.models.StatusCharField(max_length=125),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ilostatus',
            name='processor',
            field=hpilo.models.StatusCharField(max_length=125),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ilostatus',
            name='status',
            field=hpilo.models.StatusCharField(max_length=125),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ilostatus',
            name='storage',
            field=hpilo.models.StatusCharField(max_length=125),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ilostatus',
            name='temperature',
            field=hpilo.models.StatusCharField(max_length=125),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ilostatusdetail',
            name='status',
            field=hpilo.models.StatusCharField(max_length=125, null=True, blank=True),
            preserve_default=True,
        ),
    ]
