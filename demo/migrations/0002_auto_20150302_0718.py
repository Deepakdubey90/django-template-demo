# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='author',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=50),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=64),
        ),
    ]
