from django.db import models

# Create your models here.
class Cart(models.Model):
    number_of_products = models.PositiveIntegerField()
    total_amount = models.DecimalField(max_digits=6,decimal_places=2)
    shipping_cost = models.DecimalField(max_digits=6,decimal_places=2)
    payment_options = models.CharField(max_length=32)
    discount = models.DecimalField(max_digits=5,decimal_places=2)
    
    def __str__(self):
        return self.payment_options