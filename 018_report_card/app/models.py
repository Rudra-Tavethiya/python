from django.db import models

# Create your models here.

class department(models.Model):
    name = models.CharField(max_length=20)

class stid(models.Model):
    stid = models.CharField(max_length=10)

class student(models.Model):
    dept = models.ForeignKey(department,on_delete=models.CASCADE)
    stid = models.ForeignKey(stid,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    age = models.IntegerField()

class subject(models.Model):
    name = models.CharField(max_length=20)

class marks(models.Model):
    student = models.ForeignKey(student,on_delete=models.CASCADE)
    subject = models.ForeignKey(subject,on_delete=models.CASCADE)
    marks = models.IntegerField(default=0)