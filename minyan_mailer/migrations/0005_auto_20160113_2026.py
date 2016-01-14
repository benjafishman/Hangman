# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minyan_mailer', '0004_auto_20160113_1416'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='davening',
            name='email_time',
        ),
        migrations.AlterField(
            model_name='periodicmailing',
            name='crontab_string',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='periodicmailing',
            name='email_text',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='periodicmailing',
            name='mailgun_list_name',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
