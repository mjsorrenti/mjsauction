# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-18 17:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bidding', '0007_auto_20170928_0858'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bidder',
            fields=[
                ('number', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='auctionitem',
            name='current_bid',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='auctionitem',
            name='current_bidder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]