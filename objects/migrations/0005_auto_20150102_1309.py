# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('objects', '0004_hardwareobject_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hardwareobject',
            name='image',
            field=models.ImageField(height_field=b'350', width_field=b'350', null=True, upload_to=b'', blank=True),
            preserve_default=True,
        ),
    ]
