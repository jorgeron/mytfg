# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easypadel', '0009_auto_20170301_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='jugador',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
    ]