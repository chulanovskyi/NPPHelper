# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 18:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Helper', '0002_auto_20170219_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='system',
            name='info',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
