# -*- coding: utf-8 -*-
# Generated by Django 1.11.dev20161002183156 on 2016-10-25 15:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('register_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('P', 'Pending'), ('A', 'Accepted'), ('W', 'SomeThingWrong')], max_length=1)),
                ('date', models.DateTimeField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=7)),
                ('address', models.CharField(max_length=200)),
                ('postcode', models.CharField(max_length=5)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Member')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('lates_update', models.DateTimeField()),
            ],
        ),
    ]