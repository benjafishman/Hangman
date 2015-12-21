# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minyan_mailer', '0002_auto_20151220_1601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='davening_group',
            name='email',
        ),
        migrations.AlterField(
            model_name='davening_group',
            name='minyan',
            field=models.ForeignKey(to='minyan_mailer.Minyan'),
        ),
    ]
