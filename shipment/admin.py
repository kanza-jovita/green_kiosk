from django.contrib import admin
from .models import Shipment
# Register your models here.

class ShipmentAdmin(admin.ModelAdmin):
    list_display = ("location","shipment_cost","delivery_time","delivery_status")
    
admin.site.register(Shipment,ShipmentAdmin)
    
