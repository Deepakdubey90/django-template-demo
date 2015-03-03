# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0004_auto_20150303_0706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publish_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
