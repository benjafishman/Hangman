# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minyan_mailer', '0013_auto_20151223_2113'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('davening_group', models.ForeignKey(to='minyan_mailer.Davening_Group')),
                ('member', models.ForeignKey(null=True, to='minyan_mailer.Member')),
            ],
        ),
    ]
