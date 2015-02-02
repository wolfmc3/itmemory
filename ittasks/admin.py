from django.contrib import admin
from cron.management.commands.cron import cronregistry
from ittasks.management.commands.cron_tasks import Command
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
cronregistry.register(Command())