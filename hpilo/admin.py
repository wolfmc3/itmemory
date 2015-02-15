from django.contrib import admin

from hpilo.models import IloStatus, IloStatusDetail, IloNotifySetting


class IloStatusDetailAdmin(admin.TabularInline):
    model = IloStatusDetail
    extra = 0


class IloStatusAdmin(admin.ModelAdmin):
    short_description = 'Hp Ilo Statuses'

    list_display = (
        'hardwareobject',
        'time',
        'status',
    )
    inlines = [IloStatusDetailAdmin]

admin.site.register(IloStatus, IloStatusAdmin)
admin.site.register(IloNotifySetting)

from hpilo.management.commands.cron_hpilo import Command
from cron.management.commands.cron import cronregistry

cronregistry.register(Command())