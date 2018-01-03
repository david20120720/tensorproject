# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-30 00:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gname', models.CharField(max_length=50)),
                ('gtitle', models.CharField(max_length=50)),
                ('gcontents', models.TextField()),
                ('gurl', models.URLField()),
                ('gemail', models.EmailField(max_length=254)),
                ('gcdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
