# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 10:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20170131_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body_en',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]
