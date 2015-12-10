# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_statement_is_mishnah'),
    ]

    operations = [
        migrations.AddField(
            model_name='statement',
            name='is_gemara',
            field=models.BooleanField(default=False),
        ),
    ]
