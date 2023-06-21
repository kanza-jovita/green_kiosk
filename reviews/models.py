from django.db import models

# Create your models here.
class Review(models.Model):
    message = models.TextField()
    sender = models.CharField(max_length=32)
    number_of_stars = models.IntegerField()
    date = models.DateField()
    
def __str__(self):
        return self.message