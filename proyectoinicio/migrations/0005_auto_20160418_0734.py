# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-18 07:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectoinicio', '0004_auto_20160412_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=4),
        ),
    ]