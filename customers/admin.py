from django.contrib import admin

# Register your models here.
from customers.models import Customer, WorkSite

admin.site.register(Customer)
admin.site.register(WorkSite)