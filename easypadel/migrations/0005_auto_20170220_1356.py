# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easypadel', '0004_auto_20170220_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pista',
            name='color',
            field=models.CharField(choices=[('AZUL', 'Azul'), ('VERDE', 'Verde'), ('MARRON', 'Marrón')], default='AZUL', max_length=10),
        ),
        migrations.AlterField(
            model_name='pista',
            name='tipo_pared',
            field=models.CharField(choices=[('METACRILATO', 'Metacrilato'), ('CEMENTO', 'Cemento')], default='METACRILATO', max_length=20),
        ),
        migrations.AlterField(
            model_name='pista',
            name='tipo_superficie',
            field=models.CharField(choices=[('CESPED', 'Césped artificial'), ('HORMIGON', 'Hormigón poroso'), ('MOQUETA', 'Moqueta')], default='CESPED', max_length=20),
        ),
    ]
