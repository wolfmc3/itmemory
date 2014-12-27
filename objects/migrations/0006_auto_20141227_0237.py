# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('objects', '0005_hardwareobject_know_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hardwareobject',
            name='item',
            field=models.CharField(max_length=32, verbose_name=b'Codice del prodotto'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hardwareobject',
            name='know_name',
            field=models.CharField(default=b'', max_length=255, verbose_name=b'Nome breve'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hardwareobject',
            name='location',
            field=models.CharField(max_length=250, verbose_name=b'Ubicazione'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hardwareobject',
            name='name',
            field=models.CharField(max_length=300, verbose_name=b'Nome del prodotto'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hardwareobject',
            name='primary_ip',
            field=models.IPAddressField(default=b'0.0.0.0', verbose_name=b'Indirizzo IP primario'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hardwareobject',
            name='serial',
            field=models.CharField(max_length=50, verbose_name=b'numero di serie'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hardwareobject',
            name='worksite',
            field=models.ForeignKey(related_name='objects', verbose_name=b'Luogo di installazione',
                                    to='customers.WorkSite'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='settinggroup',
            name='name',
            field=models.CharField(max_length=255, verbose_name=b'Gruppo impostazioni'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='settings',
            name='hardwareobject',
            field=models.ForeignKey(verbose_name=b'Oggetto', to='objects.HardwareObject'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='settings',
            name='type',
            field=models.ForeignKey(related_name='settingstype', verbose_name=b'Tipo impostazione',
                                    to='objects.SettingsType'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='settings',
            name='value',
            field=models.TextField(max_length=5000, verbose_name=b'Valore impostato'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='settingstype',
            name='group',
            field=models.ForeignKey(related_name='settings', verbose_name=b'Gruppo impostazioni',
                                    to='objects.SettingGroup'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='settingstype',
            name='name',
            field=models.CharField(max_length=255, verbose_name=b'Tipo impostazione'),
            preserve_default=True,
        ),
    ]
