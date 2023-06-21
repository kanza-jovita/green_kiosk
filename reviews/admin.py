from django.contrib import admin
from .models import Review
# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("message","sender","number_of_stars","date")
    
admin.site.register(Review,ReviewAdmin)