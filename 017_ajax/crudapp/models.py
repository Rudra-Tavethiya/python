from django.db import models

# Create your models here.

class student(models.Model):
    uname = models.CharField(max_length=20)
    email = models.CharField(max_length=50)    
    age = models.IntegerField()
