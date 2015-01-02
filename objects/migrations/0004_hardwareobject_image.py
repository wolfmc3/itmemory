# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('objects', '0003_auto_20150102_0106'),
    ]

    operations = [
        migrations.AddField(
            model_name='hardwareobject',
            name='image',
            field=models.ImageField(height_field=350, width_field=350, null=True, upload_to=b'', blank=True),
            preserve_default=True,
        ),
    ]
