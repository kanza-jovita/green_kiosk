from django.db import models

# Create your models here.
class Payment(models.Model):
    amount = models.DecimalField(max_digits=6,decimal_places=2)
    payment_option = models.CharField(max_length=32)
    date = models.DateField()
    receipt = models.TextField()
    status = models.CharField(max_length=32)
    
def __str__(self):
        return self.amount