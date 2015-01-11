from django.contrib import admin
from ittasks.models import Task, TaskCheck, TaskCheckTemplate, TaskTemplate


class TaskCheckInline(admin.TabularInline):
    model = TaskCheck
    extra = 0


class TaskAdmin(admin.ModelAdmin):
    inlines = [TaskCheckInline]


class TaskCheckTemplateInline(admin.StackedInline):
    model = TaskCheckTemplate
    extra = 0


class TaskTemplateAdmin(admin.ModelAdmin):
    inlines = [TaskCheckTemplateInline]


admin.site.register(Task, TaskAdmin)
admin.site.register(TaskTemplate, TaskTemplateAdmin)
