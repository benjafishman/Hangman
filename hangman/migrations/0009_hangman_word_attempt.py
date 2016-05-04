# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hangman', '0008_auto_20150906_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='hangman',
            name='word_attempt',
            field=models.CharField(max_length=200, default=''),
        ),
    ]
