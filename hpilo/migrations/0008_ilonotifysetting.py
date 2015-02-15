# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hpilo', '0007_auto_20150208_1859'),
    ]

    operations = [
        migrations.CreateModel(
            name='IloNotifySetting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Nome')),
                ('type', models.CharField(default=b'exclude/status', unique=True, max_length=255, verbose_name=b'Tipo', choices=[(b'exclude/status', b'Stato diverso da'), (b'include/status', b'Stato uguale a')])),
                ('search_value', models.CharField(default=b'OK', max_length=255, verbose_name=b'Valore filtro')),
                ('include_all_data', models.BooleanField(default=True, verbose_name=b'Includi tutti i dati')),
                ('group', models.ForeignKey(related_name='hpilosetting', verbose_name=b'Destinatari mail', blank=True, to='auth.Group', null=True)),
                ('user', models.ForeignKey(related_name='hpilosetting', verbose_name=b'Destinatario mail', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Impostazione notifica HP Ilo',
                'verbose_name_plural': 'Impostazioni notifica HP Ilo',
            },
            bases=(models.Model,),
        ),
    ]
