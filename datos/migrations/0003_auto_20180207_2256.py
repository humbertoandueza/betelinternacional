# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-08 03:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datos', '0002_auto_20180207_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscripcion',
            name='estatus',
            field=models.CharField(blank=True, choices=[('0', 'Aprobado'), ('1', 'Reprobado'), ('2', 'Finalizado')], max_length=20),
        ),
    ]
