# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-13 11:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fundraisers', '0002_auto_20171213_0642'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fundraiser',
            old_name='goal',
            new_name='goal_amount',
        ),
        migrations.AddField(
            model_name='fundraiser',
            name='raised_amount',
            field=models.PositiveIntegerField(default=0),
        ),
    ]