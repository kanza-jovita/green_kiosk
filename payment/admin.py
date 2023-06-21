from django.contrib import admin
from .models import Payment
# Register your models here.
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("amount","payment_option","date","receipt","status")
    
admin.site.register(Payment,PaymentAdmin)