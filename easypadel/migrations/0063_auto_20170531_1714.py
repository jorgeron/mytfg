# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-31 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easypadel', '0062_auto_20170531_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugador',
            name='rating_victorias',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
    ]
