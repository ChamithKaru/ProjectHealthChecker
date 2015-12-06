# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('resource_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ResourceType',
            fields=[
                ('resource_type_id', models.IntegerField(serialize=False, primary_key=True)),
                ('resource_type_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sprint_name', models.CharField(max_length=200)),
                ('sprint_start_date', models.DateTimeField(verbose_name=b'sprint_start_date')),
                ('sprint_end_date', models.DateTimeField(verbose_name=b'sprint_end_date')),
            ],
        ),
        migrations.RemoveField(
            model_name='milestone',
            name='project',
        ),
        migrations.RemoveField(
            model_name='task',
            name='milestone',
        ),
        migrations.AlterField(
            model_name='project',
            name='project_end_date',
            field=models.DateTimeField(verbose_name=b'project_end_date'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_start_date',
            field=models.DateTimeField(verbose_name=b'project_start_date'),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_end_date',
            field=models.DateTimeField(verbose_name=b'task_end_date'),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_start_date',
            field=models.DateTimeField(verbose_name=b'task_start_date'),
        ),
        migrations.DeleteModel(
            name='Milestone',
        ),
        migrations.AddField(
            model_name='sprint',
            name='project',
            field=models.ForeignKey(to='project.Project'),
        ),
        migrations.AddField(
            model_name='resource',
            name='resource_type',
            field=models.ForeignKey(to='project.ResourceType'),
        ),
        migrations.AddField(
            model_name='task',
            name='sprint',
            field=models.ForeignKey(default=1, to='project.Sprint'),
            preserve_default=False,
        ),
    ]
