# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 18:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bidding', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionitem',
            name='bidding_closed',
            field=models.BooleanField(default=False),
        ),
    ]
