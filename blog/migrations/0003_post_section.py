# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='section',
            field=models.ForeignKey(to='blog.Section', null=True),
        ),
    ]
