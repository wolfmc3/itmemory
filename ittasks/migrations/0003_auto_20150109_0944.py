# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ittasks', '0002_auto_20150102_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskcheck',
            name='result',
            field=models.IntegerField(default=0, verbose_name=b'Risultato', choices=[(0, b'Non eseguito (NE)'), (1, b'Passato (PASS)'), (4, b'Passato con errori (WARN)'), (2, b'Fallito (NG)'), (3, b'Non applicabile (NA)')]),
            preserve_default=True,
        ),
    ]
