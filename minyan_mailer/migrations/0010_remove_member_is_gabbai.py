# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minyan_mailer', '0009_auto_20151222_2206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='is_gabbai',
        ),
    ]
