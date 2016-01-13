# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minyan_mailer', '0002_minyan_timezone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailing',
            name='davening_group',
        ),
        migrations.RemoveField(
            model_name='mailing',
            name='member',
        ),
        migrations.DeleteModel(
            name='Mailing',
        ),
    ]
