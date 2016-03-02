# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-13 19:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_imageuuid'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrimaryCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='SecondaryCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('primaryCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secondary', to='product.PrimaryCategory')),
            ],
        ),
        migrations.AlterField(
            model_name='imageuuid',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='product.Product'),
        ),
    ]