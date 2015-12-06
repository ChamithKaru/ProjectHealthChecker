# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_auto_20151206_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingdata',
            name='completed_project_duration',
            field=models.DecimalField(null=True, max_digits=7, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='trainingdata',
            name='cpi',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='trainingdata',
            name='developer_experience',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='trainingdata',
            name='spi',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='trainingdata',
            name='sprint_condition',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='trainingdata',
            name='task_completion',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='trainingdata',
            name='test_cases_passed',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
        ),
    ]
