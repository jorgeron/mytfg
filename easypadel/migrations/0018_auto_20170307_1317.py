# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 12:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easypadel', '0017_auto_20170306_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='pista',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pista',
            name='nombre',
            field=models.CharField(max_length=20),
        ),
    ]
