# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-23 18:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signupp',
            old_name='connum',
            new_name='contactnumber',
        ),
        migrations.RenameField(
            model_name='signupp',
            old_name='passw',
            new_name='password',
        ),
    ]
