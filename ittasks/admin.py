from django.contrib import admin
from ittasks.models import Task, TaskCheck, TaskCheckTemplate, TaskTemplate

# Register your models here.

admin.site.register(Task)
admin.site.register(TaskCheck)
admin.site.register(TaskTemplate)
admin.site.register(TaskCheckTemplate)
