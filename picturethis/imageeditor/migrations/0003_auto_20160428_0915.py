# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-28 09:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageeditor', '0002_editedphoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editedphoto',
            name='image',
            field=models.TextField(max_length=250),
        ),
    ]
