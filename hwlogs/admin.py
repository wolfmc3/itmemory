from django.contrib import admin

# Register your models here.
from hwlogs.models import HwLog


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

admin.site.register(HwLog, HwLogAdmin)