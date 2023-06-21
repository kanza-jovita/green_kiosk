from django.contrib import admin
from .models import Vendor
# Register your models here.
class VendorAdmin(admin.ModelAdmin):
    list_display = ("name","store_name","location","contact")
    
admin.site.register(Vendor,VendorAdmin)
    