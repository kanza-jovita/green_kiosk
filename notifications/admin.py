from django.contrib import admin
from .models import Notification
# Register your models here.
class NotificationAdmin(admin.ModelAdmin):
    list_display = ("message","date","notification_type")
admin.site.register(Notification,NotificationAdmin)