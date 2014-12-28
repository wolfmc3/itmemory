# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('ittasks', '0015_auto_20141227_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskcheck',
            name='result',
            field=models.IntegerField(default=0, verbose_name=b'Risultato',
                                      choices=[(0, b'non eseguito'), (1, b'passato'), (2, b'fallito')]),
            preserve_default=True,
        ),
    ]
