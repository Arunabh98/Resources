# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-29 06:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0006_course_course_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='course_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
