# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 12:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easypadel', '0002_pista_cubierta'),
    ]

    operations = [
        migrations.AddField(
            model_name='pista',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
    ]
