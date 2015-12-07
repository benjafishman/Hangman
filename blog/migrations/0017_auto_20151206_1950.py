# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_statement_gemara_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challenge',
            name='challenged_statement',
        ),
        migrations.RemoveField(
            model_name='challenge',
            name='challenger',
        ),
        migrations.RemoveField(
            model_name='challenge',
            name='gemara_post',
        ),
        migrations.RemoveField(
            model_name='challenge_resolution',
            name='challenge',
        ),
        migrations.RemoveField(
            model_name='challenge_resolution',
            name='resolver',
        ),
        migrations.AddField(
            model_name='statement',
            name='is_challenge',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='statement',
            name='is_resolution',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Challenge',
        ),
        migrations.DeleteModel(
            name='Challenge_Resolution',
        ),
    ]
