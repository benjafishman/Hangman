# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minyan_mailer', '0005_auto_20151222_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='minyans',
            field=models.ManyToManyField(null=True, blank=True, to='minyan_mailer.Minyan'),
        ),
    ]
