# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20151130_1931'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mesechta',
            old_name='seders',
            new_name='seder',
        ),
    ]
