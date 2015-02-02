from django.contrib import admin

# Register your models here.
from cron.management.commands.cron import cronregistry
from hwlogs.management.commands.cron_hwlogs import Command
from hwlogs.models import HwLog, LogFilter, LogFilterValues


class LogFilterValuesAdmin(admin.TabularInline):
    model = LogFilterValues
    extra = 0


class HwLogAdmin(admin.ModelAdmin):
    short_description = 'Logs'
    list_display = (
        'hardwareobject',
        'log_name',
        'time',
        'event_id',
        'get_level_display',
    )
    search_fields = ['message']


class LogFilterAdmin(admin.ModelAdmin):
    short_description = 'Filtri log'
    list_display = (
        'name',
        'operation',
    )
    search_fields = ['name']
    inlines = [LogFilterValuesAdmin]

admin.site.register(HwLog, HwLogAdmin)
admin.site.register(LogFilter, LogFilterAdmin)
cronregistry.register(Command())
