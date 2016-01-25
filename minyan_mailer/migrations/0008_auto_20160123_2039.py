# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minyan_mailer', '0007_periodicmailing_davening_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='periodicmailing',
            old_name='davening_id',
            new_name='davening_key',
        ),
    ]
