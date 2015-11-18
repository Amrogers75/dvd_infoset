# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DvdList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dvd_title', models.CharField(max_length=255, null=True, blank=True)),
                ('released', models.CharField(max_length=255, null=True, blank=True)),
                ('status', models.CharField(max_length=255, null=True, blank=True)),
                ('price', models.FloatField(null=True, blank=True)),
                ('rating', models.CharField(max_length=255, null=True, blank=True)),
                ('genre', models.ForeignKey(blank=True, to='main.Genre', null=True)),
                ('studio', models.ForeignKey(blank=True, to='main.Studio', null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='dvd_list',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='dvd_list',
            name='studio',
        ),
        migrations.DeleteModel(
            name='Dvd_List',
        ),
    ]
