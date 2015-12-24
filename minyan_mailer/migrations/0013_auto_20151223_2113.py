# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minyan_mailer', '0012_davening_davenign_groups'),
    ]

    operations = [
        migrations.RenameField(
            model_name='davening',
            old_name='davenign_groups',
            new_name='davening_groups',
        ),
    ]
