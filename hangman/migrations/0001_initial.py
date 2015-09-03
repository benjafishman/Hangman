# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hangman',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('word_text', models.CharField(max_length=200)),
                ('max_number_guesses', models.IntegerField(default=0)),
                ('current_guess', models.CharField(max_length=200)),
                ('current_guess_num', models.IntegerField(default=0)),
            ],
        ),
    ]
