# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-17 13:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tastes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='taste',
            options={'ordering': ['container']},
        ),
    ]
