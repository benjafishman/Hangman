# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minyan_mailer', '0006_member_minyans'),
    ]

    operations = [
        migrations.RenameField(
            model_name='minyan',
            old_name='user',
            new_name='gabbai',
        ),
        migrations.AddField(
            model_name='minyan',
            name='contact_email',
            field=models.EmailField(max_length=254, default=None),
        ),
    ]
