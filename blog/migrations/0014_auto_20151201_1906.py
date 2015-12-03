# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_remove_gemarapost_section'),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(unique=True, max_length=100)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Challenge_Resolution',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('resolution_text', models.TextField()),
                ('challenge', models.ForeignKey(to='blog.Challenge')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Statement',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('statement', models.TextField()),
                ('person', models.ForeignKey(null=True, to='blog.Person')),
            ],
        ),
        migrations.AddField(
            model_name='challenge_resolution',
            name='resolver',
            field=models.ForeignKey(to='blog.Person'),
        ),
        migrations.AddField(
            model_name='challenge',
            name='challenged_statement',
            field=models.ForeignKey(to='blog.Statement'),
        ),
        migrations.AddField(
            model_name='challenge',
            name='challenger',
            field=models.ForeignKey(null=True, to='blog.Person'),
        ),
    ]
