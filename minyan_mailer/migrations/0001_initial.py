# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Davening',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('davening_time', models.TimeField(blank=True)),
                ('days', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=1), size=None)),
                ('email_time', models.TimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-title'],
            },
        ),
        migrations.CreateModel(
            name='Davening_Group',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('mailing_list_title', models.CharField(max_length=300)),
            ],
            options={
                'ordering': ['-title'],
            },
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('davening_group', models.ForeignKey(to='minyan_mailer.Davening_Group')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('davening_groups', models.ManyToManyField(blank=True, null=True, to='minyan_mailer.Davening_Group')),
            ],
            options={
                'ordering': ['-user'],
            },
        ),
        migrations.CreateModel(
            name='Minyan',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('contact_email', models.EmailField(max_length=254, default=None)),
                ('gabbai', models.ForeignKey(to='minyan_mailer.Member')),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.AddField(
            model_name='member',
            name='minyans',
            field=models.ManyToManyField(blank=True, null=True, to='minyan_mailer.Minyan'),
        ),
        migrations.AddField(
            model_name='member',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mailing',
            name='member',
            field=models.ForeignKey(null=True, to='minyan_mailer.Member'),
        ),
        migrations.AddField(
            model_name='davening_group',
            name='minyan',
            field=models.ForeignKey(to='minyan_mailer.Minyan'),
        ),
        migrations.AddField(
            model_name='davening',
            name='minyan',
            field=models.ForeignKey(to='minyan_mailer.Minyan'),
        ),
        migrations.AddField(
            model_name='davening',
            name='primary_davening_group',
            field=models.ForeignKey(null=True, to='minyan_mailer.Davening_Group'),
        ),
    ]
