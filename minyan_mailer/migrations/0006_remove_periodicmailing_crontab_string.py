# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minyan_mailer', '0005_auto_20160113_2026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='periodicmailing',
            name='crontab_string',
        ),
    ]
