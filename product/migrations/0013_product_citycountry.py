# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-15 16:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_auto_20160215_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cityCountry',
            field=models.CharField(default='\u725b\u6d25-\u82f1\u56fd', max_length=20),
            preserve_default=False,
        ),
    ]
