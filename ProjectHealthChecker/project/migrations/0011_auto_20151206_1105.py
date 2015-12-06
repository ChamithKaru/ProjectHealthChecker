# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_auto_20151206_0131'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_actual_hours',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='task_scheduled_hours',
            field=models.IntegerField(null=True),
        ),
    ]
