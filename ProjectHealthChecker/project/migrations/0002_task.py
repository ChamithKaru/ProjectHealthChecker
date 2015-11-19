# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('task_name', models.CharField(max_length=200)),
                ('task_start_date', models.DateTimeField(verbose_name=b'tsk_start_date')),
                ('task_end_date', models.DateTimeField(verbose_name=b'tsk_end_date')),
                ('milestone', models.ForeignKey(to='project.Milestone')),
                ('project', models.ForeignKey(to='project.Project')),
            ],
        ),
    ]
