from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20)

class country(models.Model):
    name = models.CharField(max_length=50)

class state(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(country,on_delete=models.CASCADE)

class city(models.Model):
    name = models.CharField(max_length=50)
    state = models.ForeignKey(state,on_delete=models.CASCADE)