# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-03 17:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('insuranceApp', '0004_auto_20180426_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_user',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
