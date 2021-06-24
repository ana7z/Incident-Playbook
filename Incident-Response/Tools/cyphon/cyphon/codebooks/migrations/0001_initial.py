# -*- coding: utf-8 -*-
# Copyright 2017-2019 ControlScan, Inc.
#
# This file is part of Cyphon Engine.
#
# Cyphon Engine is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# Cyphon Engine is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Cyphon Engine. If not, see <http://www.gnu.org/licenses/>.
#
# Generated by Django 1.10.1 on 2017-03-20 16:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import utils.validators.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodeBook',
            fields=[
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='companies.Company')),
            ],
            options={
                'ordering': ['company'],
            },
        ),
        migrations.CreateModel(
            name='CodeName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'ordering': ['code'],
            },
        ),
        migrations.CreateModel(
            name='RealName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regex', models.CharField(help_text='The regular expression used to identify substrings that should be replaced with the code name.', max_length=255, unique=True, validators=[utils.validators.validators.regex_validator], verbose_name='regex')),
                ('rank', models.IntegerField(default=0, help_text='The order in which the regex should be searched for and replaced.')),
                ('codename', models.ForeignKey(help_text='The string that will replace the real name.', on_delete=django.db.models.deletion.CASCADE, related_name='realnames', related_query_name='realname', to='codebooks.CodeName', verbose_name='CodeName')),
            ],
            options={
                'ordering': ['rank', 'regex'],
            },
        ),
        migrations.AddField(
            model_name='codebook',
            name='codenames',
            field=models.ManyToManyField(to='codebooks.CodeName'),
        ),
    ]
