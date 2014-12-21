# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('objects', '0005_hardwareobject_know_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enabled', models.BooleanField(default=True)),
                ('hardwareobject', models.ForeignKey(related_name='hardwareobjects', to='objects.HardwareObject')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TaskCheck',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('exectime', models.DateTimeField()),
                ('result', models.BooleanField(default=False)),
                ('note', models.TextField(max_length=1000, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TaskCheckTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TaskTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('day', models.CharField(max_length=2)),
                ('month', models.CharField(max_length=2)),
                ('year', models.CharField(max_length=4)),
                ('hour', models.CharField(max_length=2)),
                ('minute', models.CharField(max_length=2)),
                ('enabled', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='taskchecktemplate',
            name='tasktemplate',
            field=models.ForeignKey(related_name='taskchecktemplates', to='ittasks.TaskTemplate'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='taskcheck',
            name='checktemplate',
            field=models.ForeignKey(related_name='checktemplates', to='ittasks.TaskCheckTemplate'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='taskcheck',
            name='task',
            field=models.ForeignKey(related_name='tasks', to='ittasks.Task'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='task',
            name='template',
            field=models.ForeignKey(related_name='templates', to='ittasks.TaskTemplate'),
            preserve_default=True,
        ),
    ]
