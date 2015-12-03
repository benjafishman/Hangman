# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20151130_1929'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gemarapost',
            old_name='mishnah',
            new_name='seder',
        ),
    ]
