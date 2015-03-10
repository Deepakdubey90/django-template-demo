# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0005_auto_20150303_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='gender',
            field=models.CharField(choices=[('M', 'M'), ('F', 'F')], default='M', max_length=2),
        ),
        migrations.AlterField(
            model_name='author',
            name='marital_status',
            field=models.CharField(choices=[('S', 'S'), ('M', 'M'), ('O', 'O')], blank=True, default='S', null=True, max_length=2),
        ),
        migrations.AlterField(
            model_name='author',
            name='published_books',
            field=models.CharField(choices=[('T', 'T'), ('M', 'M'), ('S', 'S'), ('Mg', 'Mg')], default='T', null=True, max_length=2),
        ),
    ]
