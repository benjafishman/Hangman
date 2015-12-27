# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minyan_mailer', '0015_davening_days'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='davening',
            name='day_of_week',
        ),
    ]
