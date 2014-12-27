# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('ittasks', '0014_auto_20141227_0237'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Attivit\xe0', 'verbose_name_plural': 'Attivit\xe0'},
        ),
        migrations.AlterModelOptions(
            name='taskcheck',
            options={'verbose_name': 'Controllo', 'verbose_name_plural': 'Controlli'},
        ),
        migrations.AlterModelOptions(
            name='taskchecktemplate',
            options={'verbose_name': 'Modello controllo', 'verbose_name_plural': 'Modelli controlli'},
        ),
        migrations.AlterModelOptions(
            name='tasktemplate',
            options={'verbose_name': 'Modello attivit\xe0', 'verbose_name_plural': 'Modelli attivit\xe0'},
        ),
    ]
