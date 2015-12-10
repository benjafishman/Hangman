# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20151206_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='statement',
            name='is_mishnah',
            field=models.BooleanField(default=False),
        ),
    ]
