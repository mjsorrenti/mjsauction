# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bidding', '0002_auctionitem_bidding_closed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionitem',
            name='bidding_closed',
        ),
        migrations.AddField(
            model_name='auctionitem',
            name='bidding_open',
            field=models.BooleanField(default=True),
        ),
    ]
