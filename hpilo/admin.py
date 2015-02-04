from django.contrib import admin

from hpilo.models import IloStatus, IloStatusDetail

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