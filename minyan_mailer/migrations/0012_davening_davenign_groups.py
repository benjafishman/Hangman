# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minyan_mailer', '0011_remove_davening_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='davening',
            name='davenign_groups',
            field=models.ManyToManyField(to='minyan_mailer.Davening_Group', null=True, blank=True),
        ),
    ]
