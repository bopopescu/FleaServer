# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-18 01:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0023_emailcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='nickname',
            field=models.CharField(default='DBL_Lee', max_length=254, unique=True),
            preserve_default=False,
        ),
    ]