# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2011-05-06 08:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datos', '0002_auto_20110506_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='ing_famil',
            field=models.CharField(max_length=60),
        ),
    ]
