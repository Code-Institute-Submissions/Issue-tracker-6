# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-26 21:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bio',
            name='location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
