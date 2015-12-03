# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20151130_1918'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mesechta',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('seders', models.CharField(max_length=2, choices=[('Zr', 'Zraim'), ('Mo', 'Moed'), ('Na', 'Nashim'), ('Ne', 'Nesikim'), ('Ko', 'Kodashim'), ('To', 'Toharoth')])),
            ],
        ),
        migrations.RemoveField(
            model_name='gemarapost',
            name='mesechta',
        ),
        migrations.AddField(
            model_name='gemarapost',
            name='mishnah',
            field=models.ForeignKey(to='blog.Mesechta', null=True),
        ),
    ]
