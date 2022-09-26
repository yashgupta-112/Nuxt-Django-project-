from django.db import models

# Create your models here.

class tickets(models.Model):
    user = models.CharField(max_length=255)
    email = models.CharField(max_length=255,default='')
    subject = models.CharField(max_length=255)
    priority = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    message = models.CharField(max_length=800)
   
    
    def __str__(self):
        return self.user
    
    
class guide(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=505)
   
    
    def __str__(self):
        return self.title