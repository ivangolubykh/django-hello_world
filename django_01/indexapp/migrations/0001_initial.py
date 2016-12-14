# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Learn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=1500, verbose_name='Учреждение')),
                ('site', models.CharField(max_length=128, verbose_name='Ссылка на сайт')),
                ('date_end', models.DateField(db_index=True, verbose_name='Дата окончания')),
                ('speciality', models.CharField(max_length=128, verbose_name='Специальность')),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=1500, verbose_name='Организация')),
                ('region', models.CharField(max_length=64, verbose_name='Регион')),
                ('site', models.CharField(max_length=128, verbose_name='Ссылка на сайт')),
                ('date_start', models.DateField(db_index=True, verbose_name='Дата начала работы')),
                ('date_end', models.DateField(verbose_name='Дата окончания работы')),
                ('position', models.CharField(max_length=128, verbose_name='Должность')),
                ('descr', models.TextField(verbose_name='Описание/Обязанности')),
            ],
        ),
    ]
