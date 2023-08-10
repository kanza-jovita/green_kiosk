from django.db import models
from django.contrib.auth.models import User
# from order.models import Order

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    # basket = models.ForeignKey(Order,on_delete=models.CASCADE)
    
    firstName = models.CharField(max_length=32)
    lastName = models.CharField(max_length=32)
    phoneNumber = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.firstName + "" + self.lastName
    