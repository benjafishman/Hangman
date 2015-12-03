# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_challenge_gemara_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='statement',
            name='gemara_post',
            field=models.ForeignKey(null=True, to='blog.GemaraPost'),
        ),
    ]
