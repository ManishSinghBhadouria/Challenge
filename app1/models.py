from django.db import models
from django.utils import timezone

# Create your models here.
class Registration(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    currentdate= models.DateField(default=timezone.now)

    def __str__(self):
        return self.email

class Location(models.Model):
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    currentdate= models.DateField(default=timezone.now)

    def __str__(self):
        return self.country


class Weather(models.Model):
    city=models.CharField(max_length=100)
    temp=models.CharField(max_length=100)
    temp1=models.CharField(max_length=100)
    press=models.CharField(max_length=100)
    humi=models.CharField(max_length=100)
    sdesc=models.CharField(max_length=100)
    currentdate= models.DateField(default=timezone.now)

    def __str__(self):
        return self.city