# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_gemara'),
    ]

    operations = [
        migrations.AddField(
            model_name='gemara',
            name='number_of_perakim',
            field=models.IntegerField(blank=True, null=True, default=0),
        ),
    ]
