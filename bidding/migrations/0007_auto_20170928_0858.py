# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 12:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bidding', '0006_auto_20170927_1415'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionitem',
            name='current_bid',
        ),
        migrations.RemoveField(
            model_name='auctionitem',
            name='current_bidder',
        ),
    ]
