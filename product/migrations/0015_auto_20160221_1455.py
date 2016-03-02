# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 14:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_auto_20160215_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='originalPrice',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]