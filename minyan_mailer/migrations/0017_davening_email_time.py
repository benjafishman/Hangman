# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minyan_mailer', '0016_remove_davening_day_of_week'),
    ]

    operations = [
        migrations.AddField(
            model_name='davening',
            name='email_time',
            field=models.FloatField(default=0),
        ),
    ]
