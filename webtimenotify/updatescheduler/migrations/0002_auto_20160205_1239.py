# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-05 12:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('updatescheduler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='updateevent',
            name='day_choice',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='updateevent',
            name='month_choice',
            field=models.IntegerField(default=1),
        ),
    ]
