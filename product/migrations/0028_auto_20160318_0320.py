# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-18 03:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0027_myuser_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='avatar',
            field=models.CharField(default='defaultavatar.png', max_length=50),
        ),
    ]