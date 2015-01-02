# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enabled', models.BooleanField(default=True, verbose_name=b'Abilitato')),
                ('done', models.BooleanField(default=False, verbose_name=b'Completato')),
                ('laststart', models.DateTimeField(null=True, verbose_name=b'Ultimo avvio/esecuzione', blank=True)),
                ('hardwareobject', models.ForeignKey(related_name='hardwareobjects', verbose_name=b'Hardware associato',
                                                     to='objects.HardwareObject')),
            ],
            options={
                'verbose_name': 'Attivit\xe0',
                'verbose_name_plural': 'Attivit\xe0',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TaskCheck',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('exectime', models.DateTimeField(verbose_name=b'Data di esecuzione')),
                ('result', models.IntegerField(default=0, verbose_name=b'Risultato',
                                               choices=[(0, b'Non eseguito (NE)'), (1, b'Passato (PASS)'),
                                                        (2, b'Fallito (NG)'), (3, b'Non applicabile (NA)')])),
                ('note', models.TextField(max_length=1000, null=True, verbose_name=b'Note sul controllo', blank=True)),
            ],
            options={
                'verbose_name': 'Controllo',
                'verbose_name_plural': 'Controlli',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TaskCheckTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Nome del controllo')),
                ('description',
                 models.TextField(max_length=1000, verbose_name=b"Descrizione dell'operazione da eseguire")),
            ],
            options={
                'verbose_name': 'Modello controllo',
                'verbose_name_plural': 'Modelli controlli',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TaskTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Nome')),
                ('day', models.CharField(max_length=2, verbose_name=b'Giorni')),
                ('month', models.CharField(max_length=2, verbose_name=b'Mesi')),
                ('year', models.CharField(max_length=4, verbose_name=b'Anni')),
                ('hour', models.CharField(max_length=2, verbose_name=b'Ore')),
                ('minute', models.CharField(max_length=2, verbose_name=b'Minuti')),
                ('enabled', models.BooleanField(default=True, verbose_name=b'Abilitato')),
            ],
            options={
                'verbose_name': 'Modello attivit\xe0',
                'verbose_name_plural': 'Modelli attivit\xe0',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='taskchecktemplate',
            name='tasktemplate',
            field=models.ForeignKey(related_name='taskchecktemplates', verbose_name=b'Modello di Task',
                                    to='ittasks.TaskTemplate'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='taskcheck',
            name='checktemplate',
            field=models.ForeignKey(related_name='checktemplates', verbose_name=b'Modello di task',
                                    to='ittasks.TaskCheckTemplate'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='taskcheck',
            name='task',
            field=models.ForeignKey(related_name='tasks', verbose_name=b'Task', to='ittasks.Task'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='task',
            name='template',
            field=models.ForeignKey(related_name='templates', verbose_name=b'Modello di task',
                                    to='ittasks.TaskTemplate'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='task',
            name='user',
            field=models.ForeignKey(verbose_name=b'Utente assegnato', blank=True, to=settings.AUTH_USER_MODEL,
                                    null=True),
            preserve_default=True,
        ),
    ]
