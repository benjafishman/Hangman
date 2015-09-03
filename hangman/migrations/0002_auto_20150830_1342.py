# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hangman', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hangman',
            name='max_number_guesses',
            field=models.IntegerField(default=7),
        ),
    ]
