# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20151201_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gemarapost',
            name='post_amud',
            field=models.CharField(choices=[('0', 'A'), ('1', 'B')], max_length=2),
        ),
    ]
