# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hangman', '0003_hangman_session_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hangman',
            old_name='word_text',
            new_name='word',
        ),
        migrations.AddField(
            model_name='hangman',
            name='attempts',
            field=models.CharField(max_length=200, default=''),
        ),
    ]
