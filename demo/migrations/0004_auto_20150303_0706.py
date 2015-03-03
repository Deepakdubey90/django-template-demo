# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_auto_20150303_0702'),
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
            name='id',
            field=django_extensions.db.fields.UUIDField(name='id', serialize=False, blank=True, primary_key=True, editable=False),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='authorbook',
            name='id',
            field=django_extensions.db.fields.UUIDField(name='id', serialize=False, blank=True, primary_key=True, editable=False),
        ),
        migrations.AlterField(
            model_name='book',
            name='id',
            field=django_extensions.db.fields.UUIDField(name='id', serialize=False, blank=True, primary_key=True, editable=False),
        ),
    ]
