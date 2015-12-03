# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_gemara_number_of_perakim'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gemarapost',
            name='daf',
        ),
        migrations.RemoveField(
            model_name='gemarapost',
            name='seder',
        ),
        migrations.AddField(
            model_name='gemarapost',
            name='gemara',
            field=models.ForeignKey(null=True, to='blog.Gemara'),
        ),
        migrations.AddField(
            model_name='gemarapost',
            name='post_amud',
            field=models.IntegerField(default=0, max_length=1, choices=[(0, 'A'), (1, 'B')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gemarapost',
            name='post_daf',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
