# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-31 08:45
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('easypadel', '0055_pista_visible'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pareja1set1', models.DecimalField(decimal_places=0, max_digits=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(7)])),
                ('pareja2set1', models.DecimalField(decimal_places=0, max_digits=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(7)])),
                ('pareja1set2', models.DecimalField(decimal_places=0, max_digits=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(7)])),
                ('pareja2set2', models.DecimalField(decimal_places=0, max_digits=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(7)])),
                ('pareja1set3', models.DecimalField(blank=True, decimal_places=0, max_digits=1, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(7)])),
                ('pareja2set3', models.DecimalField(blank=True, decimal_places=0, max_digits=1, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(7)])),
                ('pareja1totalSets', models.DecimalField(decimal_places=0, max_digits=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)])),
                ('pareja2totalSets', models.DecimalField(decimal_places=0, max_digits=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)])),
                ('fecha_partido', models.DateTimeField()),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empresa', to='easypadel.Empresa')),
                ('jugador1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jugador1', to='easypadel.Jugador')),
                ('jugador2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jugador2', to='easypadel.Jugador')),
                ('jugador3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jugador3', to='easypadel.Jugador')),
                ('jugador4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jugador4', to='easypadel.Jugador')),
            ],
            options={
                'verbose_name': 'Resultado',
                'verbose_name_plural': 'Resultados',
            },
        ),
    ]