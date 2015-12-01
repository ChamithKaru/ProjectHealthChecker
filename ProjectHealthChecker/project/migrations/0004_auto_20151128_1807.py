# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20151128_1352'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project', models.ForeignKey(to='project.Project')),
                ('resource', models.ForeignKey(to='project.Resource')),
                ('sprint', models.ForeignKey(to='project.Sprint')),
            ],
        ),
        migrations.CreateModel(
            name='Cost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project', models.ForeignKey(to='project.Project')),
                ('sprint', models.ForeignKey(to='project.Sprint')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='task_priority',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='assignment',
            name='task',
            field=models.ForeignKey(to='project.Task'),
        ),
    ]
