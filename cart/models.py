from django.db import models
from inventory.models import Product
from order.models import Order
# Create your models here.
class Cart(models.Model):
    products = models.ManyToManyField(Product)
    order = models.OneToOneField(Order,on_delete=models.CASCADE,null=True)
    
    number_of_products = models.PositiveIntegerField()
    total_amount = models.DecimalField(max_digits=6,decimal_places=2)
    shipping_cost = models.DecimalField(max_digits=6,decimal_places=2)
    payment_options = models.CharField(max_length=32)
    discount = models.DecimalField(max_digits=5,decimal_places=2)
    
    def __str__(self):
        return self.payment_options
    
    def add_product(self,product):
        self.products.add(product)
        self.save()
        return self
    
    def get_total(self):
        products = self.products
        total = 0
        for product in products:
            total += product.price
        return total

# add = sum([product.price for product in self.products])    