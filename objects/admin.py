from django.contrib import admin

# Register your models here.
from objects.models import HardwareObject, Settings, SettingsType, SettingGroup


class SettingsInline(admin.TabularInline):
    model = Settings
    extra = 1


class HardwareObjectAdmin(admin.ModelAdmin):
    short_description = 'Hardware objects'
    fieldsets = [
        (None, {'fields': ['name', 'item', 'serial']}),
        ('Installation place', {'fields': ['worksite', 'location']}),
        ('Other', {'fields': ['primary_ip']})
    ]
    inlines = [SettingsInline]
    list_display = ('name', 'serial', 'worksite')
    search_fields = ['name', 'serial']


admin.site.register(HardwareObject, HardwareObjectAdmin)
admin.site.register(Settings)
admin.site.register(SettingsType)
admin.site.register(SettingGroup)
