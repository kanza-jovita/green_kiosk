from django.db import models
from order.models import Order
# Create your models here.
class Shipment(models.Model):
    ship = models.ManyToManyField(Order)
    location = models.TextField()
    shipment_cost = models.DecimalField(max_digits=6,decimal_places=2)
    delivery_time = models.DateField()
    delivery_status = models.TextField()

def __str__(self):
        return self.delivery_status
    
