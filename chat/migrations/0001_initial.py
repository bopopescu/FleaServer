# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-23 02:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EaseToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=100)),
                ('expires_in', models.DateField()),
                ('application', models.CharField(max_length=50)),
            ],
        ),
    ]