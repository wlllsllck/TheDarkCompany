# -*- coding: utf-8 -*-
# Generated by Django 1.11.dev20161002183156 on 2016-10-28 16:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='member',
        ),
        migrations.DeleteModel(
            name='Member',
        ),
    ]
