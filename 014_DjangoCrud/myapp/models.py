from django.db import models

# Create your models here.
class student(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    age = models.IntegerField()
    image = models.ImageField(upload_to="studentprofile",null=True)
