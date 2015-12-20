# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minyan_mailer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='minyan',
            old_name='gabbai',
            new_name='user',
        ),
    ]
