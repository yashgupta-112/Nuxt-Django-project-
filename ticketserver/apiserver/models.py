from django.db import models

# Create your models here.

class tickets(models.Model):
    user = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    priority = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    create_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user