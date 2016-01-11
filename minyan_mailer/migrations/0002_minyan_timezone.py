# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minyan_mailer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='minyan',
            name='timezone',
            field=models.CharField(default='US/Eastern', max_length=254),
        ),
    ]
