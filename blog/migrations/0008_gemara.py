# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20151130_1935'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gemara',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('seder', models.CharField(max_length=100, unique=True)),
                ('number_of_daf', models.IntegerField(null=True, default=0, blank=True)),
            ],
        ),
    ]
