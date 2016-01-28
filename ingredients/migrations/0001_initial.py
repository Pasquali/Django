# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-26 01:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_per_unit', models.IntegerField()),
                ('unit_of_measure', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
