# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20151201_1832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gemarapost',
            name='section',
        ),
    ]
