# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('topic', models.CharField(max_length=15, default='p', choices=[('p', 'python'), ('j', 'java'), ('c', 'c++'), ('b', 'bash'), ('m', 'misc')])),
                ('author', models.CharField(max_length=30, default='s', choices=[('s', 'Sravan K Ghantasala'), ('p', 'Praveen kumar Ghantasala')])),
                ('tags', models.CharField(blank=True, max_length=100)),
                ('git_link', models.URLField()),
                ('page', models.FilePathField(max_length=200)),
                ('desc', models.TextField(blank=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('edit_time', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
