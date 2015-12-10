# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_statement_is_gemara'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageDictionary',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('hebrew_word', models.CharField(max_length=100, unique=True)),
                ('english_word', models.CharField(max_length=100, unique=True)),
                ('gemara_post', models.ForeignKey(null=True, to='blog.GemaraPost')),
            ],
        ),
    ]
