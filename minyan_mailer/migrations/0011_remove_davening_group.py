# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minyan_mailer', '0010_remove_member_is_gabbai'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='davening',
            name='group',
        ),
    ]
