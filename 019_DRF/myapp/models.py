from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    age = models.IntegerField()


class emp(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    salary = models.FloatField()
    dept = models.CharField(max_length=20)

class product(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    description = models.TextField()
    stock = models.IntegerField()