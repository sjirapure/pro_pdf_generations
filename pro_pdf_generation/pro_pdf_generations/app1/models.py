from django.db import models

# Create your models here.

class Employee(models.Model):
    eid = models.IntegerField()
    name = models.CharField(max_length=50)
    salary = models.FloatField()
    mail  = models.EmailField()
    city = models.CharField(max_length=20)