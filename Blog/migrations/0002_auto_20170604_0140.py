# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-03 23:40
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tresc',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
