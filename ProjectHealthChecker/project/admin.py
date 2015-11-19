from django.contrib import admin
from .models import Project
from .models import Milestone
from .models import Task

# Register your models here.

admin.site.register(Project)
admin.site.register(Milestone)
admin.site.register(Task)