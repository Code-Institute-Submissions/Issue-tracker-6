# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-17 16:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tickets', '0020_auto_20181215_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_tickets_form',
            name='post_like',
            field=models.ManyToManyField(blank=True, related_name='post_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
