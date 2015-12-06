from django.contrib import admin
from .models import Project,Assignment,Cost,Resource,ResourceType,Sprint,Task

# Register your models here.


admin.site.register(Project)
admin.site.register(Sprint)
admin.site.register(Task)
admin.site.register(ResourceType)
admin.site.register(Resource)
admin.site.register(Assignment)
admin.site.register(Cost)
