# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0013_project_project_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('completed_project_duration', models.DecimalField(null=True, max_digits=7, decimal_places=4)),
                ('spi', models.DecimalField(null=True, max_digits=6, decimal_places=4)),
                ('cpi', models.DecimalField(null=True, max_digits=6, decimal_places=4)),
                ('developer_experience', models.DecimalField(null=True, max_digits=5, decimal_places=4)),
                ('task_completion', models.DecimalField(null=True, max_digits=5, decimal_places=4)),
                ('test_cases_passed', models.DecimalField(null=True, max_digits=5, decimal_places=4)),
                ('sprint_condition', models.DecimalField(null=True, max_digits=5, decimal_places=4)),
                ('date', models.TimeField(auto_now_add=True)),
                ('project', models.ForeignKey(to='project.Project')),
                ('sprint', models.ForeignKey(to='project.Sprint')),
            ],
        ),
    ]
