# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20151201_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='gemara_post',
            field=models.ForeignKey(default=None, to='blog.GemaraPost'),
            preserve_default=False,
        ),
    ]
