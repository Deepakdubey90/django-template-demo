# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=100)),
                ('published_books', models.CharField(choices=[('T', 'Technical'), ('M', 'Management'), ('S', 'Story'), ('Mg', 'Magzine')], max_length=200, null=True)),
                ('dob', models.DateField(null=True)),
                ('marital_status', models.CharField(choices=[('S', 'Single'), ('M', 'Married'), ('O', 'Other')], blank=True, max_length=100, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthorBook',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('author', models.ForeignKey(to='demo.Author')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('publish_date', models.DateField(null=True)),
                ('price', models.CharField(max_length=20)),
                ('publication', models.CharField(max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='authorbook',
            name='book',
            field=models.ForeignKey(to='demo.Book'),
            preserve_default=True,
        ),
    ]
