# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-25 20:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20151225_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='link',
            field=models.CharField(choices=[('Home', 'Home'), ('Values', 'Values'), ('Participate', 'Participate'), ('Come', 'Come'), ('Contact', 'Contact'), ('Activity', 'Activity')], default='Home', max_length=24),
        ),
    ]
