# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hangman', '0005_auto_20150901_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hangman',
            name='max_number_guesses',
            field=models.IntegerField(default=7),
        ),
    ]
