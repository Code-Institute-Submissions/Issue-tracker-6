# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-10 20:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tickets', '0014_auto_20181208_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_tickets_form',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
