# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minyan_mailer', '0008_auto_20151222_2202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='minyans',
        ),
        migrations.AddField(
            model_name='member',
            name='minyans',
            field=models.ManyToManyField(blank=True, to='minyan_mailer.Minyan', null=True),
        ),
    ]
