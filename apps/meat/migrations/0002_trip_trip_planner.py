# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 17:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_manager', '0004_auto_20170929_1607'),
        ('meat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='trip_planner',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='trip', to='user_manager.User'),
            preserve_default=False,
        ),
    ]
