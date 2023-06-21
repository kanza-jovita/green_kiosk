from django.contrib import admin
from .models import Order
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ("order_number","order_total","date","products")
admin.site.register(Order,OrderAdmin)
