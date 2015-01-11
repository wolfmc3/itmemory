from django.contrib import admin

# Register your models here.
from objects.models import HardwareObject, Settings, SettingsType, SettingGroup, SoftwarePassword


class SettingsInline(admin.TabularInline):
    model = Settings
    extra = 1


class PasswordsInline(admin.TabularInline):
    model = SoftwarePassword
    extra = 1


class HardwareObjectAdmin(admin.ModelAdmin):
    short_description = 'Hardware objects'
#    fieldsets = [
#        (None, {'fields': ['name', 'item', 'serial', 'image']}),
#        ('Installation place', {'fields': ['worksite', 'location']}),
#        ('Other', {'fields': ['primary_ip', 'parentobject']})
#    ]
    inlines = [SettingsInline, PasswordsInline]
    list_display = ('name', 'serial', 'worksite', 'primary_ip')
    search_fields = ['name', 'serial']


class SettingTypeInline(admin.TabularInline):
    model = SettingsType
    extra = 1


class SettingGroupAdmin(admin.ModelAdmin):
    inlines = [SettingTypeInline]

admin.site.register(HardwareObject, HardwareObjectAdmin)
admin.site.register(SettingGroup, SettingGroupAdmin)

