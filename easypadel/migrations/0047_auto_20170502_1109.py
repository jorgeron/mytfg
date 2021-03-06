# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-02 09:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('easypadel', '0046_auto_20170502_1059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='post_ptr',
        ),
        migrations.AddField(
            model_name='comentario',
            name='fecha_publicacion',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='comentario',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='comentario_pics/%Y-%m-%d/', verbose_name='Foto'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='jugador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='easypadel.Jugador'),
        ),
    ]
