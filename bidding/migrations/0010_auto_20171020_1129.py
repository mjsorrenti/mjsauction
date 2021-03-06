# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-20 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bidding', '0009_auto_20171018_1322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bidder',
            name='user',
        ),
        migrations.AddField(
            model_name='bidder',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='bidder',
            name='first_name',
            field=models.CharField(default='John', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bidder',
            name='last_name',
            field=models.CharField(default='Doe', max_length=30),
            preserve_default=False,
        ),
    ]
