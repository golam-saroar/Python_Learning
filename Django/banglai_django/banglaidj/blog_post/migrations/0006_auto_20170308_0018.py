# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-07 18:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_post', '0005_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roll',
            field=models.IntegerField(),
        ),
    ]