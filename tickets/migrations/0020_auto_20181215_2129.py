# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-15 21:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0019_auto_20181215_2118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likes_ticket',
            name='ticket',
        ),
        migrations.RemoveField(
            model_name='likes_ticket',
            name='user',
        ),
        migrations.RemoveField(
            model_name='comment_form',
            name='upvote',
        ),
        migrations.AddField(
            model_name='add_tickets_form',
            name='like_and_dislike',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='likes_ticket',
        ),
    ]
