# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-25 13:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_doctor_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor_info',
            name='id',
        ),
        migrations.RemoveField(
            model_name='patient_info',
            name='id',
        ),
        migrations.AlterField(
            model_name='doctor_info',
            name='username',
            field=models.CharField(max_length=15, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='patient_info',
            name='username',
            field=models.CharField(max_length=15, primary_key=True, serialize=False),
        ),
    ]