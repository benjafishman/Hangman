# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('minyan_mailer', '0003_auto_20151221_1815'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('is_gabbai', models.BooleanField(default=0)),
                ('davening_groups', models.ManyToManyField(to='minyan_mailer.Davening_Group')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-user'],
            },
        ),
        migrations.AlterField(
            model_name='minyan',
            name='user',
            field=models.ForeignKey(to='minyan_mailer.Member'),
        ),
    ]
