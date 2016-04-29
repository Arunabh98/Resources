# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-29 12:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0007_resource_course_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='course_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.course'),
        ),
    ]
