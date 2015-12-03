# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_section'),
    ]

    operations = [
        migrations.CreateModel(
            name='GemaraPost',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(unique=True, max_length=100)),
                ('slug', models.SlugField(unique=True, max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('published', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('mesechta', models.CharField(unique=True, max_length=100)),
                ('daf', models.CharField(unique=True, max_length=100)),
                ('categories', models.ManyToManyField(to='blog.Category')),
                ('section', models.ForeignKey(to='blog.Section', null=True)),
            ],
            options={
                'abstract': False,
                'ordering': ['-created'],
            },
        ),
        migrations.RemoveField(
            model_name='post',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='post',
            name='section',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
