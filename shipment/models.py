from django.db import models

# Create your models here.
class Shipment(models.Model):
    location = models.TextField()
    shipment_cost = models.DecimalField(max_digits=6,decimal_places=2)
    delivery_time = models.DateField()
    delivery_status = models.TextField()

def __str__(self):
        return self.delivery_status
    
