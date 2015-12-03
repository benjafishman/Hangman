# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20151201_1829'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gemara',
            options={'ordering': ['-title']},
        ),
        migrations.RenameField(
            model_name='gemarapost',
            old_name='post_amud',
            new_name='amud',
        ),
        migrations.RenameField(
            model_name='gemarapost',
            old_name='post_daf',
            new_name='daf',
        ),
    ]
