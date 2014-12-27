# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        ('ittasks', '0013_task_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='done',
            field=models.BooleanField(default=False, verbose_name=b'Completato'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='enabled',
            field=models.BooleanField(default=True, verbose_name=b'Abilitato'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='hardwareobject',
            field=models.ForeignKey(related_name='hardwareobjects', verbose_name=b'Hardware associato',
                                    to='objects.HardwareObject'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='laststart',
            field=models.DateTimeField(null=True, verbose_name=b'Ultimo avvio/esecuzione', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='template',
            field=models.ForeignKey(related_name='templates', verbose_name=b'Modello di task',
                                    to='ittasks.TaskTemplate'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='user',
            field=models.ForeignKey(verbose_name=b'Utente assegnato', blank=True, to=settings.AUTH_USER_MODEL,
                                    null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='taskcheck',
            name='checktemplate',
            field=models.ForeignKey(related_name='checktemplates', verbose_name=b'Modello di task',
                                    to='ittasks.TaskCheckTemplate'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='taskcheck',
            name='exectime',
            field=models.DateTimeField(verbose_name=b'Data di esecuzione'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='taskcheck',
            name='note',
            field=models.TextField(max_length=1000, null=True, verbose_name=b'Note sul controllo', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='taskcheck',
            name='result',
            field=models.BooleanField(default=False, verbose_name=b'Risultato'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='taskcheck',
            name='task',
            field=models.ForeignKey(related_name='tasks', verbose_name=b'Task', to='ittasks.Task'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='taskchecktemplate',
            name='description',
            field=models.TextField(max_length=1000, verbose_name=b"Descrizione dell'operazione da eseguire"),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='taskchecktemplate',
            name='name',
            field=models.CharField(max_length=100, verbose_name=b'Nome del controllo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='taskchecktemplate',
            name='tasktemplate',
            field=models.ForeignKey(related_name='taskchecktemplates', verbose_name=b'Modello di Task',
                                    to='ittasks.TaskTemplate'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tasktemplate',
            name='day',
            field=models.CharField(max_length=2, verbose_name=b'Giorni'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tasktemplate',
            name='enabled',
            field=models.BooleanField(default=True, verbose_name=b'Abilitato'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tasktemplate',
            name='hour',
            field=models.CharField(max_length=2, verbose_name=b'Ore'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tasktemplate',
            name='minute',
            field=models.CharField(max_length=2, verbose_name=b'Minuti'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tasktemplate',
            name='month',
            field=models.CharField(max_length=2, verbose_name=b'Mesi'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tasktemplate',
            name='name',
            field=models.CharField(max_length=100, verbose_name=b'Nome'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tasktemplate',
            name='year',
            field=models.CharField(max_length=4, verbose_name=b'Anni'),
            preserve_default=True,
        ),
    ]
