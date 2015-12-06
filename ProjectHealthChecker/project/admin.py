from django.contrib import admin
from .models import Project
from .models import Sprint
from .models import Task

# Register your models here.

admin.site.register(Project)
admin.site.register(Sprint)
admin.site.register(Task)