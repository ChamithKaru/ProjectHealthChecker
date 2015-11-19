# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('milestone_name', models.CharField(max_length=200)),
                ('milestone_start_date', models.DateTimeField(verbose_name=b'mlstn_start_date')),
                ('milestone_end_date', models.DateTimeField(verbose_name=b'mlstn_end_date')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project_name', models.CharField(max_length=200)),
                ('project_start_date', models.DateTimeField(verbose_name=b'prj_start_date')),
                ('project_end_date', models.DateTimeField(verbose_name=b'prj_end_date')),
            ],
        ),
        migrations.AddField(
            model_name='milestone',
            name='project',
            field=models.ForeignKey(to='project.Project'),
        ),
    ]
