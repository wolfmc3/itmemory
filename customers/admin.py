from django.contrib import admin

# Register your models here.
from customers.models import Customer, WorkSite


class WorksiteInLine(admin.StackedInline):
    model = WorkSite
    extra = 0


class CustomerAdmin(admin.ModelAdmin):
    short_description = "Clienti"
    list_display = ('name', 'city', 'origin_code', 'email')
    search_fields = ['name', 'origin_code', 'email']
    inlines = [WorksiteInLine]

admin.site.register(Customer, CustomerAdmin)
admin.site.register(WorkSite)