# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-22 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0040_auto_20160419_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermembership',
            name='buyerfeedbacked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ordermembership',
            name='sellerfeedbacked',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='ordermembership',
            name='ongoing',
            field=models.BooleanField(default=True),
        ),
    ]
