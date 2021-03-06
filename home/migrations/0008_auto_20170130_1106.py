# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 11:06
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20170130_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body_en',
            field=wagtail.wagtailcore.fields.StreamField([('body', wagtail.wagtailcore.blocks.StructBlock([('body', wagtail.wagtailcore.blocks.CharBlock(required=True))], icon='pick'))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_fr',
            field=wagtail.wagtailcore.fields.StreamField([('body', wagtail.wagtailcore.blocks.StructBlock([('body', wagtail.wagtailcore.blocks.CharBlock(required=True))], icon='pick'))], blank=True, null=True),
        ),
    ]
