# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_auto_20151205_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingdata',
            name='completed_project_duration',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='trainingdata',
            name='cpi',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='trainingdata',
            name='developer_experience',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='trainingdata',
            name='spi',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='trainingdata',
            name='task_completion',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='trainingdata',
            name='test_cases_passed',
            field=models.IntegerField(null=True),
        ),
    ]
