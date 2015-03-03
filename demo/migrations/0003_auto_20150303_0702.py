# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_auto_20150302_0718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='author',
            name='gender',
            field=models.CharField(max_length=100, choices=[('M', 'Male'), ('F', 'Female')]),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=32),
        ),
    ]
