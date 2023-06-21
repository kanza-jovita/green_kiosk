from django.db import models

# Create your models here.
class Order(models.Model):
    order_number = models.PositiveIntegerField()
    order_total = models.DecimalField(max_digits=6,decimal_places=2)
    date = models.DateField()
    products = models.TextField()
    customer = models.CharField(max_length=100)
    
    def __str__(self):
        return self.products 
