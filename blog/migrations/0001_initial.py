# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 19:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ogrenciler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=50)),
                ('soyad', models.CharField(max_length=50)),
                ('TC', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ogrenciler2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adi', models.CharField(max_length=50)),
                ('soyadi', models.CharField(max_length=50)),
            ],
        ),
    ]
