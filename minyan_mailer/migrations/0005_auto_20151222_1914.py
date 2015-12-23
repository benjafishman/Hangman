# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minyan_mailer', '0004_auto_20151222_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='davening_groups',
            field=models.ManyToManyField(to='minyan_mailer.Davening_Group', blank=True, null=True),
        ),
    ]
