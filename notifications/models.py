from django.db import models

# Create your models here.
class Notification(models.Model):
    message = models.TextField()
    date = models.DateField()
    notification_type = models.BooleanField()
    
def __str__(self):
        return self.message