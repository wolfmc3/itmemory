# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HardwareObject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300, verbose_name=b'Nome del prodotto')),
                ('item', models.CharField(max_length=32, verbose_name=b'Codice del prodotto')),
                ('serial', models.CharField(max_length=50, verbose_name=b'numero di serie')),
                ('location', models.CharField(max_length=250, verbose_name=b'Ubicazione')),
                ('primary_ip', models.IPAddressField(default=b'0.0.0.0', verbose_name=b'Indirizzo IP primario')),
                ('know_name', models.CharField(default=b'', max_length=255, verbose_name=b'Nome breve')),
                ('worksite', models.ForeignKey(related_name='hardwareobjects', verbose_name=b'Luogo di installazione',
                                               to='customers.WorkSite')),
            ],
            options={
                'verbose_name': 'Dispositivo hardware',
                'verbose_name_plural': 'Dispositivi hardware',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SettingGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Gruppo impostazioni')),
            ],
            options={
                'verbose_name': 'Gruppo impostazioni',
                'verbose_name_plural': 'Gruppi impostazioni',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.TextField(max_length=5000, verbose_name=b'Valore impostato')),
                ('hardwareobject', models.ForeignKey(verbose_name=b'Oggetto', to='objects.HardwareObject')),
            ],
            options={
                'verbose_name': 'Impostazione',
                'verbose_name_plural': 'Impostazioni',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SettingsType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Tipo impostazione')),
                ('group', models.ForeignKey(related_name='settings', verbose_name=b'Gruppo impostazioni',
                                            to='objects.SettingGroup')),
            ],
            options={
                'verbose_name': 'Tipo impostazione',
                'verbose_name_plural': 'Tipi impostazione',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SoftwarePassword',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(null=True, verbose_name=b'Indirizzo web', blank=True)),
                ('username', models.CharField(max_length=100, null=True, verbose_name=b'Nome utente', blank=True)),
                ('password', models.CharField(max_length=50, null=True, verbose_name=b'Password', blank=True)),
                ('passwd', models.BinaryField(max_length=250, null=True, blank=True)),
                ('hardwareobject', models.ForeignKey(related_name='softwarepasswords', verbose_name=b'Oggetto',
                                                     to='objects.HardwareObject')),
                ('settingtype', models.ForeignKey(related_name='softwarepasswords', verbose_name=b'Tipo impostazione',
                                                  to='objects.SettingsType')),
            ],
            options={
                'verbose_name': 'Password',
                'verbose_name_plural': 'Passwords',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='settings',
            name='type',
            field=models.ForeignKey(related_name='settingstype', verbose_name=b'Tipo impostazione',
                                    to='objects.SettingsType'),
            preserve_default=True,
        ),
    ]
