# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-04-11 13:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='名称')),
            ],
            options={
                'verbose_name': '学科',
                'verbose_name_plural': '学科',
                'db_table': 'tb_sub',
            },
        ),
    ]
