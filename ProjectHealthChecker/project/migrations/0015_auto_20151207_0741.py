# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0014_currentdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currentdata',
            name='sprint_condition',
            field=models.CharField(default=b'pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='trainingdata',
            name='sprint_condition',
            field=models.CharField(default=b'pending', max_length=50),
        ),
    ]
