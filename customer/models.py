from django.db import models

# Create your models here.

class Customer(models.Model):
    firstName = models.CharField(max_length=32)
    lastName = models.CharField(max_length=32)
    phoneNumber = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.firstName + "" + self.lastName
    