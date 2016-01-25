# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minyan_mailer', '0006_remove_periodicmailing_crontab_string'),
    ]

    operations = [
        migrations.AddField(
            model_name='periodicmailing',
            name='davening_id',
            field=models.ForeignKey(default=None, to='minyan_mailer.Davening'),
            preserve_default=False,
        ),
    ]
