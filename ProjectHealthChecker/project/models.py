from __builtin__ import unicode
from django.db import models

# Create your models here.


class Project(models.Model):
    project_name = models.CharField(max_length=200)
    project_start_date = models.DateTimeField('project_start_date')
    project_end_date = models.DateTimeField('project_end_date')

    def __unicode__(self):
        return self.project_name


class Sprint(models.Model):
    project = models.ForeignKey(Project)
    sprint_name = models.CharField(max_length=200)
    sprint_start_date = models.DateTimeField('sprint_start_date')
    sprint_end_date = models.DateTimeField('sprint_end_date')

    def __unicode__(self):
        return self.sprint_name


class Task(models.Model):
    sprint = models.ForeignKey(Sprint)
    project = models.ForeignKey(Project)
    task_name = models.CharField(max_length=200)
    task_priority = models.IntegerField(default=1)
    task_start_date = models.DateTimeField('task_start_date')
    task_end_date = models.DateTimeField('task_end_date')
    task_scheduled_hours = models.IntegerField(null=True)
    task_actual_hours = models.IntegerField(null=True)
    task_status = models.CharField(max_length=50, default='pending')

    def __unicode__(self):
        return self.task_name


class ResourceType(models.Model):
    resource_type_id = models.IntegerField(primary_key=True)
    resource_type_name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.resource_type_name


class Resource(models.Model):
    resource_name = models.CharField(max_length=200)
    resource_type = models.ForeignKey(ResourceType)

    def __unicode__(self):
        return self.resource_name


class Assignment(models.Model):
    resource = models.ForeignKey(Resource)
    project = models.ForeignKey(Project)
    sprint = models.ForeignKey(Sprint)
    task = models.ForeignKey(Task)

    def __unicode__(self):
        return self.id


class Cost(models.Model):
    project = models.ForeignKey(Project)
    sprint = models.ForeignKey(Sprint)
    scheduled_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    actual_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __unicode__(self):
        return self.id


class TrainingData(models.Model):
    completed_project_duration = models.IntegerField(null=True)
    spi = models.IntegerField(null=True)
    cpi = models.IntegerField(null=True)
    developer_experience = models.IntegerField(null=True)
    task_completion = models.IntegerField(null=True)
    test_cases_passed = models.IntegerField(null=True)
    sprint_condition = models.IntegerField(null=True)

    def __unicode__(self):
        return unicode(self.id)