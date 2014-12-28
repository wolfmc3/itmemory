# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('ittasks', '0016_auto_20141228_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskcheck',
            name='result',
            field=models.IntegerField(default=0, verbose_name=b'Risultato',
                                      choices=[(0, b'Non eseguito (NE)'), (1, b'Passato (PASS)'), (2, b'Fallito (NG)'),
                                               (3, b'Non applicabile (NA)')]),
            preserve_default=True,
        ),
    ]
