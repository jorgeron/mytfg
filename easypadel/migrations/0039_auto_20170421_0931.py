# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-21 07:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('easypadel', '0038_auto_20170420_1347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seguimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seguidores', to=settings.AUTH_USER_MODEL)),
                ('origen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='siguiendo', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='seguimiento',
            unique_together=set([('origen', 'destino')]),
        ),
    ]
