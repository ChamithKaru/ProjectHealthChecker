__author__ = 'Thish'

from project.models import Project, Sprint, Task
from datetime import tzinfo, timedelta, datetime
import pandas as pd
from dateutil import rrule

ZERO = timedelta(0)


class UTC(tzinfo):
    def utcoffset(self, dt):
        return ZERO

    def tzname(self, dt):
        return "UTC"

    def dst(self, dt):
        return ZERO


utc = UTC()


class parameterCalculator():
    def calculateProjectCompletion(self, projectId):
        obj = Project.objects.get(pk=projectId)
        start_date = obj.project_start_date
        end_date = obj.project_end_date
        current_date = datetime.now(utc)

        delta1 = end_date - start_date
        delta2 = current_date - start_date
        # print delta1
        # print delta2
        project_duration = delta1.days
        days_passed = delta2.days
        print project_duration
        print days_passed

        completed_percentage = (float(days_passed) / float(project_duration)) * 100

        return completed_percentage


    def calculateSpi(self, projectId, sprintId):
        sprobj = Sprint.objects.filter(project_id=projectId, id=sprintId)[0]
        # for o in sprobj:
        # print o.sprint_start_date
        taskobj = Task.objects.filter(project_id=projectId, sprint_id=sprintId)
        total_scheduled_hours = 0
        total_actual_hours = 0

        for o in taskobj:
            total_scheduled_hours += o.task_scheduled_hours
            total_actual_hours += o.task_actual_hours

        start_date = sprobj.sprint_start_date
        end_date = sprobj.sprint_end_date
        current_date = datetime.now(utc)

        delta1 = end_date - start_date
        delta2 = current_date - start_date
        print delta1
        print delta2
        #sprint_duration = delta1.days
        #days_passed = delta2.days
        daygenerator = (start_date + timedelta(x + 1) for x in xrange((end_date - start_date).days))
        sprint_duration = sum(1 for day in daygenerator if day.weekday() < 5)
        daygenerator = (start_date + timedelta(x + 1) for x in xrange((current_date - start_date).days))
        days_passed = sum(1 for day in daygenerator if day.weekday() < 5)

        print sprint_duration
        print days_passed

        scheduled_hours_passed = (float(total_scheduled_hours) / float(sprint_duration)) * days_passed
        print scheduled_hours_passed
        print total_actual_hours
        spi = float(scheduled_hours_passed) / float(total_actual_hours)
        return spi


p = parameterCalculator()
print p.calculateSpi(7, 1)



