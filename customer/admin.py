from django.contrib import admin
from .models import Customer
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
  list_display = ("firstName","lastName","phoneNumber","email","address","date_created")
admin.site.register(Customer,CustomerAdmin)
    