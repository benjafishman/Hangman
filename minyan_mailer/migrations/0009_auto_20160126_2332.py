# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minyan_mailer', '0008_auto_20160123_2039'),
    ]

    operations = [
        migrations.RenameField(
            model_name='davening',
            old_name='davening_time',
            new_name='local_davening_time',
        ),
        migrations.RenameField(
            model_name='periodicmailing',
            old_name='email_send_time',
            new_name='email_local_send_time',
        ),
        migrations.AddField(
            model_name='periodicmailing',
            name='email_utc_send_time',
            field=models.TimeField(null=True, blank=True),
        ),
    ]
