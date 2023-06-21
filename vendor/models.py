from django.db import models

# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=32)
    location = models.TextField()
    store_name = models.CharField(max_length=32)
    contact = models.CharField(max_length=16)
    
    
    
    def __str__(self):
        return self.store_name
    