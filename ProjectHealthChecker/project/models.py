from django.db import models

# Create your models here.

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    project_start_date = models.DateTimeField('prj_start_date')
    project_end_date = models.DateTimeField('prj_end_date')
    def __unicode__(self):
        return self.project_name

class Milestone(models.Model):
    project = models.ForeignKey(Project)
    milestone_name = models.CharField(max_length=200)
    milestone_start_date = models.DateTimeField('mlstn_start_date')
    milestone_end_date = models.DateTimeField('mlstn_end_date')
    def __unicode__(self):
        return self.milestone_name

class Task(models.Model):
    milestone = models.ForeignKey(Milestone)
    project = models.ForeignKey(Project)
    task_name = models.CharField(max_length=200)
    task_start_date = models.DateTimeField('tsk_start_date')
    task_end_date = models.DateTimeField('tsk_end_date')
    def __unicode__(self):
        return self.task_name
