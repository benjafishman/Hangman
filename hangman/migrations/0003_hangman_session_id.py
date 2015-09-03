# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hangman', '0002_auto_20150830_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='hangman',
            name='session_id',
            field=models.CharField(default='0000000', max_length=200),
        ),
    ]
