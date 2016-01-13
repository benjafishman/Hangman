# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minyan_mailer', '0003_auto_20160112_1900'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeriodicMailing',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('email_text', models.TextField(max_length=200)),
                ('enabled', models.BooleanField()),
                ('mailgun_list_name', models.CharField(max_length=1000)),
                ('crontab_string', models.CharField(max_length=50)),
                ('crontab_schedule_id', models.CharField(max_length=200)),
                ('periodic_task_id', models.CharField(max_length=200)),
                ('email_send_time', models.TimeField(null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='davening',
            name='periodic_mailing',
            field=models.ForeignKey(null=True, to='minyan_mailer.PeriodicMailing'),
        ),
    ]
