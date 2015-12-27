# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('minyan_mailer', '0014_mailing'),
    ]

    operations = [
        migrations.AddField(
            model_name='davening',
            name='days',
            field=django.contrib.postgres.fields.ArrayField(size=None, default=['0'], base_field=models.CharField(max_length=1)),
            preserve_default=False,
        ),
    ]
