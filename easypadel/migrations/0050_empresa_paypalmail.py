# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-08 10:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easypadel', '0049_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='paypalMail',
            field=models.EmailField(default='jorgeron1993-facilitator@hotmail.com', max_length=254, verbose_name='PayPal e-mail'),
            preserve_default=False,
        ),
    ]