# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-19 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('purpose', models.CharField(max_length=250)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
