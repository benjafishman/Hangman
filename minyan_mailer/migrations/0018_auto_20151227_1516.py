# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minyan_mailer', '0017_davening_email_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='davening',
            name='davening_groups',
        ),
        migrations.AddField(
            model_name='davening',
            name='primary_davening_group',
            field=models.ForeignKey(null=True, to='minyan_mailer.Davening_Group'),
        ),
        migrations.AddField(
            model_name='davening_group',
            name='mailing_list_title',
            field=models.CharField(default='mailgun_test_davening_group', max_length=300),
            preserve_default=False,
        ),
    ]
