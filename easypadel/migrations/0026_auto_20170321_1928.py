# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-21 18:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easypadel', '0025_auto_20170320_1718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diaasignacionhorario',
            name='horario',
        ),
        migrations.RemoveField(
            model_name='diaasignacionhorario',
            name='pista',
        ),
        migrations.DeleteModel(
            name='DiaAsignacionHorario',
        ),
    ]
