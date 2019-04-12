# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-04-11 13:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAbsences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Courses', verbose_name='课程')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Student', verbose_name='学生')),
            ],
        ),
    ]
