# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 13:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20170504_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinorder',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
